<template>
    <div>
        <div class="flex flex-row items-center">
            <AddSinotrack>
                <button class="flex flex-row items-center hover:cursor-pointer bg-orange-600/40 hover:bg-orange-600/50 hover:cursor-pointer text-orange-500 p-2 rounded-md mr-4">
                    <PlusIcon class="w-5 h-5 mr-2" />
                    <span class="mr-2">Добавить SinoTrack</span>
                </button>
            </AddSinotrack>
            <button class="border p-2 text-orange-500 border-orange-600/40 rounded-md hover:bg-orange-600/10 hover:cursor-pointer">
                <FunnelIcon class="w-5 h-5" />
            </button>
            <a href="https://sinotrack.com" target="_blank" class="ml-2 border p-2 text-orange-500 border-orange-600/40 rounded-md hover:bg-orange-600/10 hover:cursor-pointer">
                <GlobeAltIcon class="w-5 h-5" />
            </a>
        </div>
 
        <div v-if="sinotracks.length >= 1" class="relative overflow-x-auto overflow-y-auto bg-neutral-primary-soft mt-4 shadow-xs rounded-md border border-orange-400 max-h-132">
            <table class="w-full text-sm text-left rtl:text-right text-body rounded-md">
                <thead class="text-sm text-orange-500 bg-orange-600/40 border-b border-orange-400 rounded-base">
                    <tr>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Серійний номер
                        </th>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Номер телефону
                        </th>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Дата оплати
                        </th>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Дата завершеня тарифу
                        </th>
                    </tr>
                </thead>
                <tbody>
                        <tr v-for="sinotrack in sinotracks" class="bg-neutral-primary border-b border-gray-400 hover:bg-gray-500/10 hover:cursor-pointer">
                            <th scope="row" class="px-6 py-4 font-medium text-heading whitespace-nowrap">
                                {{ sinotrack.number }}
                            </th>
                            <td class="px-6 py-4">
                                {{ sinotrack.phone_number }}
                            </td>
                            <td class="px-6 py-4">
                                {{ sinotrack.pay_date }}
                            </td>
                            <td class="px-6 py-4">
                                {{ sinotrack.end_date }}
                            </td>
                        </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import AddSinotrack from '../components/modals/AddSinotrackModal.vue';
import VehicleViewModal from '../components/modals/VehicleViewModal.vue';
import { PlusIcon, FunnelIcon, GlobeAltIcon, NoSymbolIcon } from '@heroicons/vue/24/outline';

const showModal = ref(true);


function addVehicleOpenModel() {
    showModal.value = true
}

function addVehicleCloseModel() {
    showModal.value = false

}


const sinotracks = [

]
</script>