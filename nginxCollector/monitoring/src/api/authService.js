import axios from "axios";
import api from "@/constants/backendApi";

class AuthService {
  login(user) {
    return axios
      .post(api.LOGIN, {
        email: user.email,
        password: user.password
      })
      .then(response => {
        if (response.data.access) {
          localStorage.setItem("user", JSON.stringify(response.data));
        }
        return response.data;
      });
  }

  logout() {
    localStorage.removeItem("user");
  }

  register(user) {
    return axios.post(api.REGISTER, {
      username: user.username,
      email: user.email,
      password: user.password,
      password2: user.password2
    });
  }
}

export default new AuthService();
