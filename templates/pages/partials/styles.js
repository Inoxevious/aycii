    <script src="{% static 'assets/vendor/jquery/jquery.min.js' %}"></script>
    <script src="{% static 'assets/vendor/jquery-migrate/jquery-migrate.min.js' %}"></script>
    <script src="{% static 'assets/vendor/popper.js' %}/popper.min.js' %}"></script>
    <script src="{% static 'assets/vendor/bootstrap/bootstrap.min.js' %}"></script>

    <!-- JS Implementing Plugins -->
    <script src="{% static 'assets/vendor/hs-megamenu/src/hs.megamenu.js' %}"></script>
    <script src="{% static 'assets/vendor/jquery-ui/ui/widget.js' %}"></script>
    <script src="{% static 'assets/vendor/jquery-ui/ui/widgets/menu.js' %}"></script>
    <script src="{% static 'assets/vendor/jquery-ui/ui/widgets/mouse.js' %}"></script>
    <script src="{% static 'assets/vendor/jquery-ui/ui/widgets/slider.js' %}"></script>
    <script src="{% static 'assets/vendor/chosen/chosen.jquery.js' %}"></script>
    <script src="{% static 'assets/vendor/slick-carousel/slick/slick.js' %}"></script>
    <script src="{% static 'assets/vendor/fancybox/jquery.fancybox.min.js' %}"></script>

    <!-- JS Unify -->
    <script src="{% static 'assets/js/hs.core.js' %}"></script>
    <script src="{% static 'assets/js/components/hs.header.js' %}"></script>
    <script src="{% static 'assets/js/helpers/hs.hamburgers.js' %}"></script>
    <script src="{% static 'assets/js/components/hs.dropdown.js' %}"></script>
    <script src="{% static 'assets/js/components/hs.slider.js' %}"></script>
    <script src="{% static 'assets/js/components/hs.select.js' %}"></script>
    <script src="{% static 'assets/js/components/hs.carousel.js' %}"></script>
    <script src="{% static 'assets/js/components/hs.popup.js' %}"></script>
    <script src="{% static 'assets/js/components/hs.go-to.js' %}"></script>
    

    <!-- JS Customization -->
    <script src="{% static 'assets/js/custom.js' %}"></script>

    <!-- JS Plugins Init. -->
    <script>
      $(document).on("ready", function () {
        // initialization of header
        $.HSCore.components.HSHeader.init($("#js-header"));
        $.HSCore.helpers.HSHamburgers.init(".hamburger");

        // initialization of HSMegaMenu component
        $(".js-mega-menu").HSMegaMenu({
          event: "hover",
          pageContainer: $(".container"),
          breakpoint: 991,
        });

        // initialization of HSDropdown component
        $.HSCore.components.HSDropdown.init($("[data-dropdown-target]"), {
          afterOpen: function () {
            $(this).find('input[type="search"]').focus();
          },
        });

        // initialization of range slider
        $.HSCore.components.HSSlider.init("#rangeSlider1");

        // initialization of custom select
        $.HSCore.components.HSSelect.init(".js-custom-select");

        // initialization of carousel
        $.HSCore.components.HSCarousel.init('[class*="js-carousel"]');

        // initialization of popups
        $.HSCore.components.HSPopup.init(".js-fancybox");

        // initialization of go to
        $.HSCore.components.HSGoTo.init(".js-go-to");
      });
    </script>