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
  <div class="project">
  <el-row :gutter="40" style="margin-right: 15px;margin-left: -5px" type="flex" v-loading="loading">
    <el-col v-for="(item, index) in projects" :key="index" :span="8">
      <el-card class="box-card" :body-style="{ padding: '0px' }">
        <img class="image"
        :style="{backgroundImage:'url(http://bj.chinavolunteer.mca.gov.cn/subsite/static/img/0099.7c7d246.png)',backgroundSize:'cover',backgroundRepeat:'no- repeat',backgroundPosition:'center center'}">
        <div class="card-context">
          <div class="text-title">{{ item.name }}</div>
          <div class="text_item">{{ item.position }} {{ item.time }}</div>
          <div class="operate">
            <el-button @click="viewProject(item.id)" type="text">查看详情</el-button>
            <el-button @click="joinInProject(item.id)" type="text">加入项目</el-button>
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
      url: 'http://localhost:8000/buaa_db/get_project/',
      headers: {'Content-Type': 'multipart/form-data'},
    }).then((res)=>{
      console.log(res)
      this.projects = res.data.projects;
    })
  },
  data() {
    return {
      projects : [
        {id:1, name:"活动一",position:"操场", time:"2023-10-18", description: "", status: ""},
        {id:2, name:"活动二",position:"主楼", time:"2023-10-21", description: "", status: ""},
        {id:3, name:"活动一",position:"操场", time:"2023-10-18", description: "", status: ""},
        {id:4, name:"活动二",position:"主楼", time:"2023-10-21", description: "", status: ""},
        {id:5, name:"活动一",position:"操场", time:"2023-10-18", description: "", status: ""},
        {id:6, name:"活动二",position:"主楼", time:"2023-10-21", description: "", status: ""},
        {id:7, name:"活动二",position:"主楼", time:"2023-10-21", description: "", status: ""},
      ]
    }
  },
  methods: {
    viewProject(id) {
      this.$router.push({
        path: '/project/' + id
      })
    },
    joinInProject(id) {
      this.axios({
        method: 'post',
        url: 'http://localhost:8000/buaa_db/stu_apply_project_in/',
        headers: {'Content-Type': 'multipart/form-data'},
        data: {
          "project_id": id
        }
      }).then((res)=>{
        if (res.data.status == 200) {
          this.$message({
            type: 'success',
            message: "申请加入成功"
          });
        } 
        else {
          this.$message({
            type: 'error',
            message: "你已加入过该项目"
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

  .project {
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