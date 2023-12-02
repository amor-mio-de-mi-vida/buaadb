const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
module.exports = {
  devServer: {
    port:8000,
    proxy: {
      '/api':{
        target:`http://localhost:8000/buaa_db/`, //请求后台接口
        changeOrigin:true, // 允许跨域
        pathRewrite:{
            '^/api' : '' // 重写请求
        }
      }
    }
  }
}
