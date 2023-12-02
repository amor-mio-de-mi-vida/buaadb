import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueAxios from 'vue-axios'
import axios from 'axios'

axios.defaults.withCredentials=true
 
Vue.use(ElementUI);
Vue.use(VueAxios, axios)
Vue.config.productionTip = false
 
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})