import axios from 'axios';
import { ref } from 'vue';

const api_url = import.meta.env.VITE_API_URL

export var sinotracks = ref([])

export async function getAllSinotrack() {
    try {
        const resp = await axios.get(`${api_url}/api/sinotracks/all`);
        if (resp.status !== 200) {
            return resp.statusText;
        }
        return resp.data;
        
    } catch (err) {
        console.error("Ошибка при получении Sinotracks:", err)
        return null;
    }
}

export async function getAvailableSinotracks() {
    try {
        const resp = await axios.get(`${api_url}/api/sinotracks/available`)
        return resp.data;
    } catch (err) {
        console.error("Ошибка при получении Sinotracks:", err)
        return [];
    }
}

export async function addSinotrack(id, phone_number, pay_date) {
    try {
        const resp = await axios.post(`${api_url}/api/sinotracks/add`, {
            _id: id,
            phone_number: phone_number,
            payment_date: pay_date
        })
        console.log(resp)
        return resp;
    } catch (err) {
        console.log(err)
    }
}