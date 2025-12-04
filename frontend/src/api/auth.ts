import { jwtDecode } from 'jwt-decode'
import axios from 'axios';
import router from '../router';

const api_url = import.meta.env.VITE_API_URL

export function getToken() {
  return localStorage.getItem('access')
}

export function isAuthenticated() {
  const token = getToken()
  if (!token) return false

  try {
    const decoded = jwtDecode(token)
    const now = Date.now() / 1000
    return decoded.exp && decoded.exp > now // токен не истёк
  } catch {
    return false
  }
}

export function logout() {
  localStorage.removeItem('access')
}

export function login(email: string, password: string) {
    axios.post(`${api_url}/api/token/`, {
        email: email,
        password: password
    })
    .then((resp) => {
        if (resp.status === 200) {
            localStorage.setItem("access", resp.data.access)
            router.push("/")
        }
    })
    .catch(function (error) {
        return error;
    });
}