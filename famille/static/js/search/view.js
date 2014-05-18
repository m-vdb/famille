var notifier = require("../notifier.js");

var constructFilterForString = function(name, query, value){
    return name + "__" + query + "=" + value;
};

var constructFilter = function(name, query, value){
    if (_.isString(value)) return constructFilterForString(name, query, value);
    if (_.isArray(value)) return _.map(value, _.partial(constructFilterForString, name, query)).join("&");
};

var constructTarifFilter = function (name, value) {
    var min = value[0];
    var max = value[1];
    if(min !== max) {
        return "tarif__gte="+ min +"&tarif__lte=" + max;
    }
};


var constructAgeFilter = function(name, value) {
    var birhdayField = "birthday";
    var today = new Date();
    var birthDate;
    switch(value) {
        case "16-":
            birthDate = new Date(today.setYear(today.getYear() - 16));
            return birhdayField + "__gte="+ birthDate.toISOString().split('T')[0];
        case "18-":
            birthDate = new Date(today.setYear(today.getYear() - 18));
            return birhdayField + "__gte="+ birthDate.toISOString().split('T')[0];
        case "18+":
            birthDate = new Date(today.setYear(today.getYear() - 18));
            return birhdayField + "__lte="+ birthDate.toISOString().split('T')[0];
        default:
            return "";
    }
};

module.exports = Backbone.View.extend({
    events: {
        "click .next": "displayNext",
        "click .previous": "displayPrevious",
        "click .favorite": "toggleFavorite",
        "click .choose-search": "switchSearch",
        "change .form-search .form-control": "doSearch",
        "click .form-search [type=checkbox]": "doSearch",
        "onkeyup .form-search [type=text]": "doSearch",
        "slideStop #id_tarif": "doSearch",
        "click .form-search [data-distance]": "doDistanceSearch",
        "change #search-sort": "doSearch",
        "change #id_age": "doSearch",
        "click .contact-result": "checkRights",
        "click .signal-result": "signalUser",
        "click .rate-result": "rateUser",
    },

    initialize: function(options){
        this.resultTemplate = options.resultTemplate;
        this.userPlan = options.userPlan;
        _.bindAll(this, "displayResults", "formatResult", "displayNext", "displayPrevious", "toggleFavorite");
        this.$distanceButton = this.$(".control-distance");
        this.$distanceInput = this.$("#id_distance");
        this.$distanceButtonGroup = this.$(".btn-group-distance");
        this.$sortSelect = this.$("#search-sort");
        if (!this.isAuthenticated()) {
            this.disableForm();
        }
    },

    buildQuery: function($els){
        var filters = $els.map(function(){
            var $this = $(this),
                name = $this.attr("name"),
                value = $this.val(),
                query = $this.data("api");
            if (value && name == "age") return constructAgeFilter(name, value);
            if (value && query) return constructFilter(name, query, value);
            if (value && name == "tarif") return constructTarifFilter(name, $this.slider("getValue"));
        });
        filters.push(this.getSortQuery());
        return _.compact(filters).join("&");
    },

    doSearch: function(){
        var $els = this.$(".form-control,[type=checkbox]:checked,#id_distance", ".form-search");
        famille.router.doSearch(this.buildQuery($els), {
            success: this.displayResults,
            error: this.error
        });
    },

    doDistanceSearch: function (e) {
        e.preventDefault();
        var $target = $(e.target),
            distance = $target.data("distance");

        if ($target.is(this.$distanceButton) && this.$distanceButton.hasClass("active")) {
            this.$distanceInput.val("");
            this.$distanceButton.removeClass("active");
            this.$distanceButtonGroup.tooltip("destroy");
            this.$distanceButton.blur();
        }
        else {
            this.$distanceInput.val(distance);
            this.$distanceButton.addClass("active");
            this.$distanceButtonGroup.tooltip({
                placement: "right",
                title: "La recherche par géolocation est active."
            });
        }
        this.doSearch();
    },

    displayNext: function(e){
        e.preventDefault();
        if (famille.router.next) {
            famille.router.doSearch(famille.router.next, {
                success: this.displayResults,
                error: this.error
            });
        }
    },

    displayPrevious: function(e){
        e.preventDefault();
        if (famille.router.previous) {
            famille.router.doSearch(famille.router.previous, {
                success: this.displayResults,
                error: this.error
            });
        }
    },

    displayResults: function(data){
        var $container = this.$(".search-results"), $noResults = this.$(".no-results");
        $container.html("");
        if (!data.length) {
            $noResults.show();
        }
        else {
            $noResults.hide();
            $container.append(_.map(data, this.formatResult));
            $("[data-toggle=popover]", $container).popover();
            $("[data-toggle=tooltip]", $container).tooltip();
            this.displayPagination();
            this.markFavoritedItems();
        }
    },

    displayPagination: function(){
        var nbResults = famille.router.total;
        this.$(".total-search-results").html(nbResults);
        this.$(".plural-search-result").html(nbResults > 1 ? "s": "");
        if (!famille.router.next) this.$(".next").addClass("disabled");
        else this.$(".next").removeClass("disabled");
        if (!famille.router.previous) this.$(".previous").addClass("disabled");
        else this.$(".previous").removeClass("disabled");
    },

    formatResult: function(object){
        return object.template;
    },

    error: function(jqXHR){
        notifier.error("Une erreur est survenue, veuillez réessayer ultérieurement.");
    },

    disableForm: function () {
        var postalCode = this.$(".form-control[name=pc]")[0];
        this.$("#id_tarif").slider('disable');
        this.attachDisabledPopover(this.$(".slider-disabled"));
        _.each(this.$(".form-control,[type=checkbox]", ".form-search"), function (el) {
            if (el === postalCode) return;

            var $el = $(el);
            if (el.tagName == "SELECT") {
                $el.select2("readonly", true);
            }
            else {
                $el.prop("disabled", "disabled");
            }
            this.attachDisabledPopover($el);
        }, this);
    },
    /**
     * Attach the popover to the elements that are disabled.
     * in order to notify the user that he can create an account.
     */
    attachDisabledPopover: function ($el) {
        $el.attr("data-toggle", "popover");
        if ($el.attr("type") === "checkbox") {
            $el = $el.parent();
        }
        $el.popover({
            placement: "bottom",
            trigger: "click",
            title: "Fonctionalité indisponible",
            content: "Créez un compte pour pouvoir l'utiliser :-)"
        });
    },

    /****************************************/
    /************      Sort     *************/
    /****************************************/

    getSortQuery: function () {
        var sort = this.$sortSelect.val();
        return "order_by=" + sort;
    },

    /****************************************/
    /************   Favorites   *************/
    /****************************************/

    initFavorites: function(){
        if (!this.isAuthenticated()) return;
        famille.userData.favorites = this.$(".favorited-item").map(function(idx, el){
            var $el = $(el);
            return "/api/v1/" + $el.data("type").toLowerCase() + "s/" + $el.data("id") + "/";
        }).get();
        this.markFavoritedItems();
    },

    markFavoritedItems: function(){
        if (!this.isAuthenticated()) return;
        var self = this;
        _.each(famille.userData.favorites, function(uri){
            self.$(".one-search-result:contains("+ uri +") .favorite .glyphicon")
            .addClass("favorited");
        });
    },

    toggleFavorite: function(e){
        if (!this.isAuthenticated()) return;
        var $target = $(e.target),
        $star = $(".glyphicon", $target),
        resource_uri = $("[data-field=resource_uri]", $target.parents(".one-search-result")).html(),
        action = ($star.hasClass("favorited")) ? "remove": "add";

        $star.toggleClass("favorited");
        if (action == "add") famille.userData.favorites.push(resource_uri);
        else famille.userData.favorites = _.without(famille.userData.favorites, resource_uri);

        famille.router.toggleFavorite({
            data: {
                resource_uri: resource_uri,
                action: action
            },
            error: this.error
        });
    },

    isAuthenticated: function(){
        return window._auth;
    },

    switchSearch: function(e){
        famille.router.switchSearch($(e.target).data("search"));
    },

    /****************************************/
    /*************   Actions   **************/
    /****************************************/

    /**
     * Verify that the user as the right to perform actions
     */
    checkRights: function (e) {
        if (this.userPlan !== "premium") {
            var $target = $(e.target);
            e.preventDefault();
            e.stopPropagation();
            $target.popover("show");
            return false;
        }
        return true;
    },

    rateUser: function (e) {
        this.checkRights(e);
    },

    signalUser: function (e) {
        if (this.checkRights(e)) {
            var $target = $(e.target);
            $target.popover("destroy");
            $target.attr("data-title", "Signaler un utilisateur");
            $target.attr("data-content", "Pourquoi voulez-vous signaler cette utilisateur ?");
            $target.popover("show");
        }
    }
});
