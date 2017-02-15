(function(exports) {
  exports.clickTab = function(tab) {
    // highlight tab
    var tabs = tab.closest(".wizard").find("ul.nav-tabs li");
    tabs.removeClass("active");
    tab.parent().addClass("active");

    exports.selectPane(tab.attr("href"));
  }

  exports.selectPane = function(pane_id) {
    // show pane
    var pane = $(pane_id);
    pane.parent().find(".wizard-pane").removeClass("active");
    pane.addClass("active");
  }

  exports.nextPane = function(button) {
    var pane = $(button).closest(".wizard-pane");
    var next_pane_href = "#" + pane.next(".wizard-pane").attr("id");
    var tabs = pane.closest(".wizard").find("ul.nav-tabs li");
    var tab = tabs.find("a[href=" + next_pane_href + "]");
    exports.clickTab(tab);
  }

  exports.initTabs = function() {
    $('.nav-tabs a').click(function(e) {
      exports.clickTab($(this));

      // prevent jump to link
      e.preventDefault();
    });
  }
})(this.wizardTabs = {});
