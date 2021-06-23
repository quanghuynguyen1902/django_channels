import Vue from "vue";
import Vuex from "vuex";
import core from "./modules/coreui";
import filter from "./modules/filter";
import { auth } from "./modules/auth";
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    core,
    filter
  }
});
