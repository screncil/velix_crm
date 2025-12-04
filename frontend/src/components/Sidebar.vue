<template>
    <aside
        class="fixed sidebar top-0 left-0 z-9999 flex h-screen w-[290px] flex-col overflow-y-auto border-r border-gray-200 bg-white px-5 transition-all duration-300 xl:static xl:translate-x-0 dark:border-gray-800 dark:bg-black -translate-x-full"
    >
        <!-- SIDEBAR HEADER -->
        <div class="sidebar-header flex items-center gap-2 pt-8 pb-7 justify-between">
            <a href="/">
                <span class="logo">
                    <img src="https://velix.com.ua/content/images/2/200x100l50nn0/19945050466328.webp" alt="velix_logo" height="100" width="150"></img>
                </span>
            </a>
        </div>
        <!-- SIDEBAR HEADER -->
        <div class="no-scrollbar flex flex-col overflow-y-auto">
            <nav>
                <div>
                    <h3 class="mb-4 text-xs leading-[20px] text-gray-400 uppercase">Меню</h3>
                    <ul class="mb-6 flex flex-col gap-1">
                        <li class="hover:bg-gray-200 rounded-md" 
                            :class="[
                            isActive(menu.path)
                            ? 'bg-orange-600/40 hover:bg-orange-600/50  text-orange-500'
                            : ''
                        ]" v-for="(menu, key) in menuGroup" :key="key">
                            <a :href="menu.path">
                                <div class="p-2 flex flex-row items-center">
                                    <component class="w-5 h-5" :is="menu.icon"/>
                                    <span class="ml-2">{{ menu.title }}</span>
                                </div>
                            </a>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    </aside>
</template>


<script setup lang="ts">
import { useRoute } from 'vue-router';
import { 
    Squares2X2Icon,
    CircleStackIcon,
    UserGroupIcon,
    TruckIcon,
    FolderIcon,
    ChartBarIcon
} from '@heroicons/vue/24/outline';
 
const menuGroup = [
    {
        name: "dashboard",
        title: "Дашборд",
        path: "/",
        icon: Squares2X2Icon
    },
    {
        name: "rent",
        title: "Оренда",
        path: "/rent",
        icon: CircleStackIcon
    },
    {
        name: "vehicles",
        title: "Парк",
        path: "/vehicles",
        icon: TruckIcon
    },
    {
        name: "stock",
        title: "Склад",
        path: "/stock",
        icon: FolderIcon
    },
    {
        name: "clients",
        title: "Клієнти",
        path: "/clients",
        icon: UserGroupIcon
    },
    {
        name: "Sinotrack",
        title: "Sinotrack",
        path: "/sinotracks",
        icon: ChartBarIcon
    }
];
const route = useRoute();

const isActive = (path: any) => route.path === path;
</script>
