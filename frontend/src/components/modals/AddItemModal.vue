<template>
  <div class="">
    <button
      type="button"
      @click="openModal"
      class=""
    >
      <slot></slot>
    </button>
  </div>
  <TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">
      <TransitionChild
        as="template"
        enter="duration-300 ease-out"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="duration-200 ease-in"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-black/25" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-y-auto">
        <div
          class="flex mt-8 min-h-full items-center justify-center p-4 text-center"
        >
          <TransitionChild
            as="template"
            enter="duration-300 ease-out"
            enter-from="opacity-0 scale-95"
            enter-to="opacity-100 scale-100"
            leave="duration-200 ease-in"
            leave-from="opacity-100 scale-100"
            leave-to="opacity-0 scale-95"
          >
            <DialogPanel
              class="w-full max-w-md transition overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
            >
              <DialogTitle
                as="h3"
                class="text-lg font-medium leading-6 text-gray-900"
              >
                Добавити товар
              </DialogTitle>
              <div v-if="error" class="p-4 mb-4 mt-4 text-sm text-red-500 rounded bg-red-400/15" role="alert">
                <span class="font-medium">Помилка!</span>   Зверніться до адміністратора для вирішення проблеми
              </div>
              <div class="text-gray-500">
                <div class="mt-3">
                  <label for="name" class="text-gray-500 text-sm">Найменування</label>
                  <input @change="handleButton" v-model="fio" type="text" id="name" class="outline-none border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-md placeholder:text-body focus:shadow-orange-500/30 focus:border-orange-500"  required placeholder="Колодки гальмівні для велосипеда Shimano,Tektro(VIQ-003) 35мм*30мм*20мм"/>
                </div>
                <div class="mt-3">
                  <label for="name" class="text-gray-500 text-sm">Код товару</label>
                  <input @change="handleButton" v-model="fio" type="text" id="name" class="outline-none border border-1 border-gray-500 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-md placeholder:text-body focus:shadow-orange-500/30 focus:border-orange-500"  required placeholder="VIQ-003"/>
                </div>
                <div class="mt-2">
                    <label for="model" class="text-gray-500 text-sm">Категорія</label>
                    <Listbox v-model="selectedCategory">
                      <div class="relative mt-1">
                          <ListboxButton
                          class="relative w-full h-11 cursor-default rounded-md border border-1 border-gray-500 bg-white py-3 pl-3 pr-10 text-left shadow-md focus:border-orange-500 focus:shadow-orange-500/30 focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white/75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 sm:text-sm"
                          >
                          <span class="block truncate">{{ selectedCategory.name }}</span>
                          <span
                              class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2"
                          >
                              <ChevronUpDownIcon
                              class="h-5 w-5 text-gray-400"
                              aria-hidden="true"
                              />
                          </span>
                          </ListboxButton>
                          <transition
                          leave-active-class="transition duration-100 ease-in"
                          leave-from-class="opacity-100"
                          leave-to-class="opacity-0"
                          >
                          <ListboxOptions
                              class="mt-1 max-h-60 w-full overflow-y-auto bg-white py-1 text-base shadow-lg ring-1 ring-black/5 focus:outline-none sm:text-sm"
                          >
                              <ListboxOption
                              v-slot="{ active, selected }"
                              v-for="category in categories"
                              :key="category.id"
                              :value="category"
                              as="template"
                              >
                              <li
                                  :class="[
                                  active ? 'bg-orange-500/40 text-orange-500' : 'text-gray-900',
                                  'relative cursor-default select-none py-2 pl-10 pr-4',
                                  ]"
                              >
                                  <span
                                  :class="[
                                      selected ? 'font-medium' : 'font-normal',
                                      'block truncate',
                                  ]"
                                  >{{ category.name }}</span
                                  >
                                  <span
                                  v-if="selected"
                                  class="absolute inset-y-0 left-0 flex items-center pl-3 text-orange-500"
                                  >
                                  <CheckIcon class="h-5 w-5" aria-hidden="true" />
                                  </span>
                              </li>
                            </ListboxOption>
                          </ListboxOptions>
                        </transition>
                      </div>
                    </Listbox>
                </div>
                <div class="mt-2">
                  <label for="model" class="text-gray-500 text-sm">Опис товару</label>
                  <textarea @change="handleButton" v-model="comment" type="date" id="model" class="'border border-1 border-gray-500 min-h-10 mt-2 text-heading text-sm rounded-md block w-full px-3 py-2.5 shadow-md focus:shadow-orange-500/30 placeholder:text-body focus:border-orange-500 outline-none" placeholder="Характеристики..." required />
                </div>
                <div class="mt-2">
                  <label for="fop-class" class="text-gray-500 text-sm mt">ФОП?</label>
                  <div id="fop-class" class="flex flex-row mt-1">
                    <div class="flex flex-row mr-3">
                      <input id="default-radio-1" type="radio" value="" name="default-radio" class="w-5 h-5 hover:cursor-pointer text-orange-500 focus:ring-1 border-default-medium bg-neutral-secondary-medium rounded-full checked:border-brand focus:bg-orange-100 focus:outline-none focus:ring-brand-subtle border border-default appearance-none focus:border-orange-500">
                      <label for="default-radio-1" class="select-none ms-2 text-sm font-medium text-heading">Так</label>
                    </div>
                    <div class="flex flex-row">
                        <input checked id="default-radio-2" type="radio" value="" name="default-radio" class="w-5 h-5 text-orange-500 hover:cursor-pointer focus:ring-1 border-default-medium bg-neutral-secondary-medium rounded-full checked:border-brand focus:bg-orange-100 focus:outline-none focus:ring-brand-subtle border border-default appearance-none focus:border-orange-500">
                        <label for="default-radio-2" class="select-none ms-2 text-sm font-medium text-heading">Ні </label>
                    </div>
                  </div>
                </div>
                <button
                  type="button"
                  :class="[activeBtn ? 'w-full inline-flex justify-center rounded-md border border-orange-600 px-4 py-2 text-sm font-medium text-orange-600 hover:bg-orange-600/40 hover:cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2 mt-3' : 'mt-3 w-full inline-flex justify-center rounded-md border border-gray-400 px-4 py-2 text-sm font-medium text-gray-400 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2']"
                  @click="Test"
                  :disabled="!activeBtn"
                >
                  Зберегти
                </button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref } from 'vue'
import {
  TransitionRoot,
  TransitionChild,
  Dialog,
  DialogPanel,
  DialogTitle,
} from '@headlessui/vue'

import {
  Listbox,
  ListboxLabel,
  ListboxButton,
  ListboxOptions,
  ListboxOption,
} from '@headlessui/vue'
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/vue/20/solid'

import { addClient, clients } from '../../api/client'
import { getAllCategories } from '../../api/category'


const isOpen = ref(false)

const selectedCategory = ref('')
const categories = ref([])


var error = false;

function closeModal() {
  isOpen.value = false
  clearFields()
}
async function openModal() {
  const category = await getAllCategories()
  categories.value = category
  isOpen.value = true
}

const activeBtn = ref(false);

const fio_input_err = ref(false)
const number_input_err = ref(false)

function clearFields(){
  number_input_err.value = false
  fio_input_err.value = false
  fio.value = ""
  number_phone.value = ""
  comment.value = ""
  selectedWhereKnow.value = ""
}


function handleButton() {
  if (fio.value.length < 10) {
    fio_input_err.value = true
    return;
  } else if (fio.value.length == 0) {
    fio_input_err.value = false;
  } else {
    fio_input_err.value = false;
  }

  if (number_phone.value.length != 0) {
    if (number_phone.value.length != 13) {
        number_input_err.value = true
        activeBtn.value = false;
        return;
    } else {
      number_input_err.value = false;
    }
  } else {
    number_input_err.value = false;
    return;
  }

  activeBtn.value = true;
}

async function Test() {
  const resp = await addClient(fio.value, number_phone.value, comment.value, selectedWhereKnow.value.id)
  console.log(resp)
  if (resp.status != 201) {
    error = true;
    return;
  }

  clients.value.push({fio: fio.value, phone_number: number_phone.value, where_know:{name: selectedWhereKnow.value.name}, comment: comment.value})

  closeModal()

  activeBtn.value = false;
  fio.value = ""
  number_phone.value = ""
  comment.value = ""
}

const fio = ref("");
const number_phone = ref("")
const comment = ref("")
var whereknows = ref([])
</script>
