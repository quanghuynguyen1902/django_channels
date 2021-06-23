import Vue from "vue";
import App from "./App.vue";
import "@/plugins/coreui.js";
import "@/plugins/paginate.js";
import "@/plugins/vueClipBoard";
import "@/plugins/vueCodeHighlight";
import router from "./router";
import store from "./store/index";
import { iconsSet as icons } from "./assets/icons/icons.js";
Vue.config.productionTip = false;

import "@/assets/styles/style.scss";
Vue.config.productionTip = false;
Vue.config.performance = true;

new Vue({
  router,
  icons,
  store,
  render: h => h(App)
}).$mount("#app");
