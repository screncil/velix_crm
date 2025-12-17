import { createWebHistory, createRouter } from 'vue-router'

import { isAuthenticated } from '../api/auth'


const routes = [
  { path: '/', component: () => import('../views/Dashboard.vue') },
  { path: '/login', component: () => import('../views/LoginView.vue') },
  { path: '/vehicles', component: () => import('../views/VehiclesView.vue') },
  { path: '/sinotracks', component: () => import('../views/SinotrackView.vue') }
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