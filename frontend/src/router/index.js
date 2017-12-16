import Vue from 'vue'
import Meta from 'vue-meta'
import Router from 'vue-router'
import MatchPage from '@/pages/Match'
import MatchHistoryPage from '@/pages/MatchHistory'
import AboutPage from '@/pages/About'
import NotFoundPage from '@/pages/NotFound'

Vue.use(Meta)
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'match history',
      component: MatchHistoryPage
    },
    {
      path: '/:package',
      component: MatchHistoryPage
    },
    {
      path: '/match/:region/:id',
      name: 'match',
      component: MatchPage
    },
    {
      path: '/about',
      name: 'about',
      component: AboutPage
    },
    {
      path: '*',
      component: NotFoundPage
    }
  ]
})
