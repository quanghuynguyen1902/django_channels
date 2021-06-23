const filter = {
  state: {
    method: "GET",
    user_id: "",
    time: "",
    url: ""
  },
  getters: {
    getMethod(state) {
      return state.method;
    },
    getUserId(state) {
      return state.user_id;
    },
    getTime(state) {
      return state.time;
    },
    getUrl(state) {
      return state.url;
    }
  },
  mutations: {
    setMethod(state, payload) {
      state.method = payload;
    },
    setUserId(state, payload) {
      state.user_id = payload;
    },
    setTime(state, payload) {
      state.time = payload;
    },
    setUrl(state, payload) {
      state.url = payload;
    }
  }
};

export default filter;
