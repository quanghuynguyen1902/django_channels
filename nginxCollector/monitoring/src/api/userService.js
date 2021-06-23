import axios from "axios";
import authHeader from "./authHeader";

class UserService {
  getUserBoard(api) {
    return axios.get(api, { headers: authHeader() });
  }
}

export default new UserService();
