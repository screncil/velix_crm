<template>
    <div>
        <div class="flex flex-row items-center">
            <AddItemModal>
                <button class="flex flex-row items-center hover:cursor-pointer bg-orange-600/40 hover:bg-orange-600/50 hover:cursor-pointer text-orange-500 p-2 rounded-md mr-4">
                    <PlusIcon class="w-5 h-5 mr-2" />
                    <span class="mr-2">Добавити товар</span>
                </button>
            </AddItemModal>
        </div>
 
        <div v-if="items.length >= 1" class="relative overflow-x-auto overflow-y-auto bg-neutral-primary-soft mt-4 shadow-xs rounded-md border border-orange-400 max-h-132">
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
                        <th scope="col" class="px-6 py-3 font-medium">
                            Використовується?
                        </th>
                    </tr>
                </thead>
               
            </table>
        </div>
        <div v-else class="relative text-center mt-10 text-gray-500">
            Наразі немає жодного товару
        </div>
    </div>
</template>

<script>
import AddItemModal from '../../components/modals/AddItemModal.vue';
import { PlusIcon } from '@heroicons/vue/24/outline';

    export default {
    components: {
       AddItemModal, PlusIcon
    },
    data() {
        return {
            items: []
        }
    }
}
</script>