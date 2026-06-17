import { createWebHistory, createRouter } from 'vue-router'

import { isAuthenticated } from '../api/auth'


const routes = [
  { path: '/', component: () => import('../views/Dashboard.vue') },
  { path: '/login', component: () => import('../views/LoginView.vue') },
  { path: '/vehicles', component: () => import('../views/VehiclesView.vue') },
  { path: '/sinotracks', component: () => import('../views/SinotrackView.vue') },
  { path: '/clients', component: () => import('../views/clients/ClientsView.vue') },
  { path: '/client/:id(\\d+)', name: 'client-detail', component: () => import('../views/clients/ClientView.vue'), props: true },
  { path: '/stock', component: () => import('../views/stock/StocksView.vue') },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('../views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const loggedIn = isAuthenticated()

  if (to.meta.requiresAuth && !loggedIn) {
    next('/login')
  } else {
    next()
  }
})

export default router