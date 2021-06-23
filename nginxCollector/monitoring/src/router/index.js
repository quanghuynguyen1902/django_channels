import Vue from "vue";
import VueRouter from "vue-router";
import Paths from "@/constants/paths";
import Container from "@/Container/Container";
import Dashboard from "@/views/Dashboard";
import Users from "@/views/Users";
import UserDetail from "@/views/UserDetail";
import Login from "@/views/Login";
import Register from "@/views/Register";
import Page404 from "@/views/Page404";
import Information from "@/components/Information";
import InstallPlugin from "@/views/InstallPlugin";
Vue.use(VueRouter);

const routes = [
  {
    path: Paths.HOME,
    name: "Home",
    component: Container,
    children: [
      {
        path: Paths.DASHBOARD,
        name: "Dashboard",
        component: Dashboard
      },
      {
        path: Paths.USERS,
        name: "Users",
        component: Users
      },
      { path: Paths.USER_DETAILS, component: UserDetail },
      {
        path: Paths.INFORMATION,
        name: "Information",
        component: Information
      },
      {
        path: Paths.PLUGIN,
        name: "Plugin",
        component: InstallPlugin
      }
    ]
  },
  {
    path: Paths.LOGIN,
    name: "Login",
    component: Login
  },
  {
    path: Paths.REGISTER,
    name: "Register",
    component: Register
  },
  { path: "*", component: Page404 }
];

const router = new VueRouter({
  mode: "history",
  routes
});

router.beforeEach((to, from, next) => {
  const publicPages = ["/login", "/register"];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem("user");

  // trying to access a restricted page + not logged in
  // redirect to login page
  if (authRequired && !loggedIn) {
    next("/login");
  } else {
    next();
  }
});

export default router;
