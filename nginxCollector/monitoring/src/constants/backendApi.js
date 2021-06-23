const api = {
  LOGIN: `${process.env.VUE_APP_Backend}/api/token/`,
  REGISTER: `${process.env.VUE_APP_Backend}/api/register/`,
  DASHBOARD: `${process.env.VUE_APP_Backend}/api/requests-data/`,
  DASHBOARD_FILTER: `${process.env.VUE_APP_Backend}/api/requests-data/filter/`,
  USERS: `${process.env.VUE_APP_Backend}/api/requests-data/users/`,
  USER_DETAILS: `${process.env.VUE_APP_Backend}/api/requests-data/user-detail/`,
  REQUESTS_ANALYTIC: `${process.env.VUE_APP_Backend}/api/requests-data/request-analytic/`,
  API_KEY: `${process.env.VUE_APP_Backend}/api/api-key/`,
  INFORMATION: `${process.env.VUE_APP_Backend}/api/get-user/`,
  NOTIFICATION_COUNT: `${process.env.VUE_APP_Backend}/api/notification_count/`,
  NOTIFICATION: `${process.env.VUE_APP_Backend}/api/notification/`
};

export default api;
