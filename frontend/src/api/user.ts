import axios from 'axios';

const api_url = import.meta.env.VITE_API_URL

export async function getUser() {
    const token = localStorage.getItem("access")
    if (!token) return null

    try {
        const resp = await axios.get(`${api_url}/api/users/me/`, {
            headers: { Authorization: `Bearer ${token}` }
        })
        return resp.data;
    } catch (err) {
        console.error("Ошибка при получении пользователя:", err)
        return null
    }
}