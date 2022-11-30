import Vue from "vue";
import Vuetify from "vuetify/lib/framework";
import colors from "vuetify/lib/util/colors";
import Toast from "vue-toastification";
import VueCookies from "vue-cookies-reactive";
import "vue-toastification/dist/index.css";

Vue.use(Vuetify);
Vue.use(VueCookies);

Vue.$cookies.config("3d");

Vue.use(Toast, {
  transition: "Vue-Toastification__bounce",
  maxToasts: 20,
  newestOnTop: true,
});

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#039BE5",
        primaryDark: "#039BE5",
        secondary: "#5E35B1",
        accent: colors.shades.black,
        error: colors.red.accent3,
        customBackground: "#F5F5F5",
      },
      dark: {
        primary: "#6ee090",
        primaryDark: "#3caf5e",
        secondary: "#66B3FF",
        customBackground: "#212121",
      },
    },
    dark: true,
  },
});
