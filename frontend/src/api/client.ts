import axios from 'axios';
import { ref } from 'vue';

const api_url = import.meta.env.VITE_API_URL

export var clients = ref([

])

export async function allClients() {
    try {
        const resp = await axios.get(`${api_url}/api/clients/all`)
        return resp.data;
    } catch (err) {
        console.log(err)
    }
}

export async function addClient(fio, phone_number, comment, where_know) {
    try {
        const resp = await axios.post(`${api_url}/api/clients/add`, {
            fio: fio,
            phone_number: phone_number,
            comment: comment,
            where_know: where_know
        })
        console.log(resp)
        return resp;
    } catch (err) {
        console.log(err)
    }
}
