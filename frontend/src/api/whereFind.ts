
import axios from 'axios';

const api_url = import.meta.env.VITE_API_URL

export async function allWhereKnow() {
    try {
        const resp = await axios.get(`${api_url}/api/whereknow/all`);
        if (resp.status !== 200) {
            return [];
        }
        return resp.data;
        
    } catch (err) {
        console.error("Ошибка при получении:", err)
        return [];
    }
}