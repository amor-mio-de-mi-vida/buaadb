<template>
  <div>
    <div>
      <homeHeader v-show="isNormal()"></homeHeader>
      <managerHomeHeader v-show="isManager()"></managerHomeHeader>
      <sysManagerHomeHeader v-show="isSys()"></sysManagerHomeHeader>
    </div>
    <div >
      <el-card class="message_card">
        <el-row>
          <el-col span="4">
            <div class="card_title">消息中心</div>
          </el-col>
          <el-col span="2" offset="17">
            <el-button type="text" icon="el-icon-edit-outline" @click="toMessageList()">
              消息列表
            </el-button>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <div class="card_content">
          <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="发送范围">
                <el-radio v-model="form.type" label="0" @change="handleRadioChange()">团队</el-radio>
                <el-radio v-model="form.type" label="1" @change="handleRadioChange()">项目</el-radio>
              <el-select v-model="form.receiver" placeholder="请选择">
                <div v-for="(item, index) in list" :key="index">
                  <el-option :label="item.name" :value="item.id"></el-option>
                </div>
              </el-select>
            </el-form-item>
            <el-form-item label="内容">
              <el-input type="textarea" :rows="10" v-model="form.content" class="send-text"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit()">立即发送</el-button>
              <el-button>取消</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
  import homeHeader from "@/components/homeHeader";
  import managerHomeHeader from "@/components/managerHomeHeader";
  import sysManagerHomeHeader from "@/components/sysManagerHomeHeader";
  export default {
    components: {homeHeader, managerHomeHeader, sysManagerHomeHeader},
    async created() { //创建时需要获取该管理员管理的全部团队，在点击团队后选择项目
      await this.axios({
        method: 'post',
        url: 'http://localhost:8000/buaa_db/get_manage_teams/'
      }).then((res)=>{
        this.teams = res.data.teams;
      })
    },
    data() {
      return {
        form: {
          type: '',
          receiver: '',
          content: ''
        },
        teams: [],
        projects: [],
        list:[]
      }
    },
    methods: {
      isNormal() {
        console.log(this.$route.query.role);
        if (this.$route.query.role === "normal_user") {
          return true;
        }
        else {
          return false;
        }
      },
      isManager() {
        if (this.$route.query.role === 'manager') {
          return true;
        }
        return false
      },
      isSys() {
        if (this.$route.query.role === 'sysManager') {
          return true;
        }
        return false
      },
      handleRadioChange() {
        if (this.form.type == '0') {
          this.list = this.teams
        }
        else {
          this.list = this.projects
        }
      },
      toMessageList() {
        this.$router.push({path: '/check_message/', query:{role:this.$route.query.role}});
      },
      onSubmit() {
        this.axios({
          method: 'post',
          url: 'http://localhost:8000/buaa_db/pub_notice/',
          headers: {'Content-Type': 'multipart/form-data'},
          data: {
            'type': this.form.type,
            'receiver': this.form.receiver,
            'text': this.form.content
          }
        }).then((res)=>{
          if (res.data.status == 200) {
            this.$message({
              message: '发送成功',
              type: 'success'
            })
          }
        })
      }
    }
  }
</script>

<style scoped>
  .message_card {
    margin-top: 15px;
    margin-left: 200px;
    margin-right: 200px;
    height: 600px;
  }

  .text {
    font-size: 14px;
  }

  .item {
    padding: 18px 0;
  }

  .box-card {
    width: 480px;
    margin-bottom: 20px;
  }
  .card_title {
    margin-left: 30px;
    margin-top: 8px;
    font-size: large;
  }
  .card_content {
    height: 500px;
  }
  .el-divider--horizontal{
    margin: 10px;
  }
  .el-divider--vertical{
    display:inline-block;
    width:1px;
    height:500px;
    margin:0 8px;
    vertical-align:middle;
    position:relative;
  }
  .el-badge {
    margin-bottom: 0;
    padding: 0;
  }
  .send-text {
    width: 70%;
  }
</style>