<template>
  <div class="home1">
      <div class="homeHeader">
      <!--向子组件传数据-->
      <homeHeader></homeHeader>
      </div>
      <!--div class="carousel">
          <div class="block">
              <span class="demonstration"></span>
              <el-carousel height="150px">
                    <el-carousel-item v-for="item in 4" :key="item">
                      <h3 class="small">{{ item }}</h3>
                    </el-carousel-item>
              </el-carousel>
          </div>
      </div-->
      <!--筛选项目-->
      <div class="select">
  
      </div>
      <div class="Team">
      <el-row :gutter="40" style="margin-right: 15px;margin-left: -5px" type="flex" v-loading="loading">
          <el-col v-for="(item, index) in teams" :key="index" :span="8">
              <el-card class="box-card" :body-style="{ padding: '0px' }">
                  <img class="image"
                  :style="{backgroundImage:'url(http://bj.chinavolunteer.mca.gov.cn/subsite/static/img/11.fb64916.png)',backgroundSize:'cover',backgroundRepeat:'no- repeat',backgroundlocation:'center center'}">
                  <div class="card-context">
                      <div class="text-title">{{ item.name }}</div>
                      <div class="text_item">{{ item.location }} {{ item.time }}</div>
                      <div class="operate">
                          <el-button @click="viewTeam(item.id)" type="text">查看详情</el-button>
                          <el-button @click="joinInTeam(item.id)" type="text">加入团体</el-button>
                      </div>    
                  </div>
              </el-card>
          </el-col>
  </el-row>
  </div>
  </div>
  </template>
  
  <script>
  import homeHeader from "@/components/homeHeader";
  export default {
      components: {homeHeader},
      async created() {
          await this.axios({
            method: 'post',
            url: 'http://localhost:8000/buaa_db/get_teams/',
            headers: {'Content-Type': 'multipart/form-data'},
          }).then((res)=>{
            this.teams = res.data.teams;
          })
      },
      data() {
        return {
            teams : [
                {id:1, name:"团体1"},
                {id:2, name:"团体2"},
                {id:3, name:"团体3"},
                {id:4, name:"团体4"},
                {id:5, name:"团体5"},
                {id:6, name:"团体6"},
            ]
        }
      },
      methods: {
          viewTeam(id) {
              this.$router.push({
                  path: '/team/' + id
              })
          },
          joinInTeam(id) {
            this.axios({
              method: 'post',
              url: 'http://localhost:8000/buaa_db/apply_team_in/',
              headers: {'Content-Type': 'multipart/form-data'},
              data: {
                  'team_id': id
              }
            }).then((res)=>{
              if (res.data.status == 200) {
                let msg = this.$message({
                  type: 'success',
                  message: "申请加入成功"
                });
                setTimeout(()=> {
                  msg.close();
                },1000);
              } else {
                this.$message({
                  type: 'error',
                  message: "你已加入过该团体"
                })
              }
          })
        }
      }
  }
  </script>
  
  <style scoped>
      .image {
          width: 100%;
          height: 180px;
          display: block;
          background-size: cover;
          background-position: center center;
      }
      .card-context {
          margin-left: 20px;
          margin-top: 10px;
          line-height: 25px;
      }
      .text-title {
          font-size: larger;
          font-weight: bold;
      }
      .text_item {
          margin-top: 10px;
      }
  
      .Team {
          margin-top: 30px;
          margin-left: 120px;
          margin-right: 120px;
      }
  
      .text {
          font-size: 14px;
      }
  
      .el-row {
      display:flex;
      flex-wrap: wrap;
      align-items: center;
    }
    .el-row  .el-card {
      width: 100%;
      height: 100%;
      margin-right: 20px;
          margin-bottom: 30px;
      transition: all .5s;
    }
  
      .clearfix:before,
      .clearfix:after {
      display: table;
      content: "";
      }
      .clearfix:after {
      clear: both
      }
  
      .box-card {
      width: 480px;
      }
  
      .carousel {
          margin-left: 120px;
          margin-right: 120px;
          text-align: center;
      }
  
      .el-carousel__item h3 {
          color: #475669;
          font-size: 14px;
          opacity: 0.75;
          line-height: 150px;
          margin: 0;
      }
  
      .el-carousel__item:nth-child(2n) {
      background-color: #99a9bf;
      }
      
      .el-carousel__item:nth-child(2n+1) {
      background-color: #d3dce6;
      }
  </style>