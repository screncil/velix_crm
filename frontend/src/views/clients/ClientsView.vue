<template>
    <div>
        <div class="flex flex-row items-center">
            <AddClientModal>
                <button class="flex flex-row items-center hover:cursor-pointer bg-orange-600/40 hover:bg-orange-600/50 hover:cursor-pointer text-orange-500 p-2 rounded-md mr-4">
                    <PlusIcon class="w-5 h-5 mr-2" />
                    <span class="mr-2">Добавити клієнта</span>
                </button>
            </AddClientModal>
            <button v-if="clients.length >= 2" class="border p-2 text-orange-500 border-orange-600/40 rounded-md hover:bg-orange-600/10 hover:cursor-pointer">
                <FunnelIcon class="w-5 h-5" />
            </button>
        </div>
 
        <div v-if="clients.length >= 1" class="relative overflow-x-auto overflow-y-auto bg-neutral-primary-soft mt-4 shadow-xs rounded-md border border-orange-400 max-h-132">
            <table class="w-full text-sm text-left rtl:text-right text-body rounded-md">
                <thead class="text-sm text-orange-500 bg-orange-600/40 border-b border-orange-400 rounded-base">
                    <tr>
                        <th scope="col" class="px-6 py-3 font-medium">
                            ПІБ
                        </th>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Номер телефону
                        </th>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Коментар
                        </th>
                        <th scope="col" class="px-6 py-3 font-medium">
                            Звідки дізнався
                        </th>
                    </tr>
                </thead>
                <tbody>
                        <tr @dblclick="gotoClientPage(client.id)" v-for="client in clients" class="bg-neutral-primary border-b border-gray-400 hover:bg-gray-500/10 hover:cursor-pointer">
                            <th scope="row" class="px-6 py-4 font-medium text-heading whitespace-nowrap">
                                {{ client.fio }}
                            </th>
                            <td class="px-6 py-4">
                                {{ client.phone_number }}
                            </td>
                            <td class="px-6 py-4">
                                {{ client.comment }}
                            </td>
                            <td v-if="client.where_know != null" class="px-6 py-4">
                                {{ client.where_know.name }}
                            </td>
                        </tr>
                </tbody>
            </table>
        </div>
        <div v-else class="relative text-center mt-10 text-gray-500">
            Наразі немає жодного клієнту
        </div>
    </div>
</template>

<script lang="ts">

import { PlusIcon, FunnelIcon, GlobeAltIcon, NoSymbolIcon, XMarkIcon, CheckIcon } from '@heroicons/vue/24/outline';

import { clients, allClients } from '../../api/client';
import AddClientModal from '../../components/modals/AddClientModal.vue'


export default {
    components: {
        PlusIcon, FunnelIcon, GlobeAltIcon, NoSymbolIcon, XMarkIcon, CheckIcon, clients, AddClientModal, allClients
    },
    data() {
        return {
            clients: clients
        }
    },
    methods: {
        gotoClientPage(id) {
            this.$router.push({
                name: 'client-detail',
                params: { id }
            })
        }
    },
    async mounted() {
        const client = await allClients();
        this.clients = client;
        console.log(this.clients)
    }
}

</script>