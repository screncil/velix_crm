import { ref } from 'vue';
import axios from 'axios';

const api_url = import.meta.env.VITE_API_URL

export async function getAllCategories() {
    try {
        const resp = await axios.get(`${api_url}/api/category/all`)
        if (resp.status !== 200) {
            console.error(resp.statusText)
            return [];
        } else {
            return resp.data;
        }
    } catch (err) {
        console.error("Ошибка при получении Categories:", err)
        return [];
    }
}