<template>
    <div>
        <div class="flex flex-row items-center">
            <AddVehicle>
                <button class="flex flex-row items-center hover:cursor-pointer bg-orange-600/40 hover:bg-orange-600/50 hover:cursor-pointer text-orange-500 p-2 rounded-md mr-4">
                    <PlusIcon class="w-5 h-5 mr-2" />
                    <span class="mr-2">Добавить транспорт</span>
                </button>
            </AddVehicle>
            <button class="border p-2 text-orange-500 border-orange-600/40 rounded-md hover:bg-orange-600/10 hover:cursor-pointer">
                <FunnelIcon class="w-5 h-5" />
            </button>
        </div>
 
        <div v-if="bikes.length > 0" class="relative overflow-x-auto overflow-y-auto bg-neutral-primary-soft mt-4 shadow-xs rounded-md border border-orange-400 max-h-132">
            <table class="w-full text-sm text-left rtl:text-right text-body rounded-md">
                <thead class="text-sm text-orange-500 bg-orange-600/40 border-b border-orange-400 rounded-base">
                    <tr>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Найменування
                        </th>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Модель
                        </th>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Серійний номер
                        </th>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Діаметр колес
                        </th>
                        <th scope="col" class="px-6 py-2 font-medium">
                            Коментарій
                        </th>
                        <th scope="col" class="px-6 py-2 font-medium">
                            В оренді
                        </th>
                        <th scope="col" class="px-6 py-2 font-medium">
                            SinoTrack
                        </th>
                    </tr>
                </thead>
                <tbody>
                        <tr v-for="bike in bikes" class="bg-neutral-primary border-b border-gray-400 hover:bg-gray-500/10 hover:cursor-pointer">
                                <th scope="row" class="px-6 py-4 font-medium text-heading whitespace-nowrap">
                                    {{ bike.name }}
                                </th>
                                <td class="px-6 py-4">
                                    {{ bike.model }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ bike.serial_number }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ bike.wheel_diameter }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ bike.comments }}
                                </td>
                                <td v-if="!bike.in_rent" class="px-6 py-4">
                                    <XMarkIcon class="text-red-500 w-5 h-5"/>
                                </td>
                                <td v-else class="px-6 py-4">
                                    <CheckIcon class="text-green-500 w-5 h-5"/>
                                </td>
                                <td v-if="bike.sinotrack != null" class="px-6 py-4 border-0">
                                    <span>{{ bike.sinotrack._id }}</span>
                                </td>
                                <td v-else class="px-6 py-4 border-0">
                                    <XMarkIcon class="text-red-500 w-5 h-5"/>
                                </td>
                        </tr>
                </tbody>
            </table>
        </div>
        <div v-else class="relative text-center mt-10 text-gray-500">
            Наразі немає жодного транспорту
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import AddVehicle from '../components/modals/AddVehicleModal.vue';
import VehicleViewModal from '../components/modals/VehicleViewModal.vue';
import { PlusIcon, FunnelIcon, XMarkIcon,CheckIcon } from '@heroicons/vue/24/outline';
import { bikes, getAllBikes } from '../api/bike';

const showModal = ref(true);


function addVehicleOpenModel() {
    showModal.value = true
}

function addVehicleCloseModel() {
    showModal.value = false

}

onMounted(() => {
    getAllBikes();
})

</script>