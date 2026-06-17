import { ref } from 'vue';
import axios from 'axios';

const api_url = import.meta.env.VITE_API_URL

export var bikes = ref([])


export async function getAllBikes() {
    try {
        const resp = await axios.get(`${api_url}/api/bikes/all`)
        if (resp.status !== 200) {
            console.error(resp.statusText)
            return bikes;
        }
        bikes.value = resp.data;
        console.log(bikes.value)
        return;
    } catch (err) {
        console.error("Ошибка при получении Sinotracks:", err)
        return [];
    }
}

export async function AddBike(name, model, serial_number, wheel_diameter, comments, sinotrack, sinotrack_id) {
    if (sinotrack == undefined) {
        try {
            const resp = await axios.post(`${api_url}/api/bikes/add`, {
                name: name,
                model: model,
                serial_number: serial_number,
                wheel_diameter: wheel_diameter,
                comments: comments
            })
            if (resp.status == 201) {
                bikes.value.push({name: name, model: model, serial_number: serial_number, wheel_diameter: wheel_diameter, comments: comments, sinotrack: null})
                return {"added": true}
            }
            else return {"added": false, "err": resp.data}
        } catch (err) {
            return {"added": false, "err": err}
        }
    }
    try {
        const resp = await axios.post(`${api_url}/api/bikes/add`, {
            name: name,
            model: model,
            serial_number: serial_number,
            wheel_diameter: wheel_diameter,
            comments: comments,
            sinotrack: sinotrack
        })
        if (resp.status == 201) {
            bikes.value.push({name: name, model: model, serial_number: serial_number, wheel_diameter: wheel_diameter, comments: comments, sinotrack: sinotrack_id})
            return {"added": true}
        }
        else return {"added": false}
    } catch (err) {
        return {"added": false, "err": err.response.data}
    }
    
}