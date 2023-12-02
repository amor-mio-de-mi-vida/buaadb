<template>
    <div id="building">
        <div class="head">
            <router-link :to="'/login'" style="text-decoration: none;">
                <h1>Home</h1>
            </router-link>
        </div>
        <div class="login-box">
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span class="login-title">🔐北航志愿实践星管理系统</span>
            </div>
            <el-form :model="form" status-icon :rules="rules" ref="form" label-width="100px" class="demo-form">
                <el-form-item label="学工号" prop="id">
                  <el-input v-model="form.id" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                  <el-input type="password" v-model="form.password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="我是" prop="role">
                  <el-select v-model="form.role" placeholder="请选择">
                    <el-option
                      v-for="item in options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                  </el-select>  
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm('form')">登录</el-button>
                    <router-link :to="'/register/'" class="button1" style="text-decoration:none">
                        <el-button>注册</el-button>
                    </router-link>
                </el-form-item>
            </el-form>
          </el-card>
        </div>
    </div>
</template>
    
<script>
    export default {
      data() {
        return { 
          options: [
            {
              value: '0',
              label: '普通用户'
            }, {
              value: '1',
              label: '志愿管理员'
            }, {
              value: '2',
              label: '系统管理员'
            }
          ],
          form: {
            role: '',
            password: '',
            id: ''
          },
          rules: {
            id: [
              { required: true, message: '请输入学工号', trigger: 'blur' },
            ],
            password : [
              { required: true, message: '请输入密码', trigger: 'blur' },
            ],
            role: [
              { required: true, message: '请选择身份', trigger: 'blur' },
            ]
          }
        };
      },
      methods: {
        submitForm(formName) {
          this.$refs[formName].validate(async (valid) => {
            valid = true;
            if (valid) {
              await this.axios({
                method: 'post',
                credentials: 'include',
                url: 'http://localhost:8000/buaa_db/login/',
                headers: {'Content-Type': 'multipart/form-data'},
                data: {
                  id : this.form.id,
                  password : this.form.password,
                  role: this.form.role
                },
                timeout: 1000
              }).then(async (res)=>{
                if (res.data.status === 200) {
                  let msg = this.$message({
                    type: 'success',
                    message: "登录成功"
                  });
                  setTimeout(()=> {
                    msg.close();
                  },1000);
                  if (this.form.role == 0) {
                    this.$router.push({path: '/home/'})
                  }
                  else if (this.form.role == 1) {
                    this.$router.push({path:'/ManageTeam/'})
                  }
                  else {
                    this.$router.push({path:'/CheckCreateProjectApply/'})
                  }
                } else if (res.data.status == 300) {
                  this.$message({
                    type: 'error',
                    message: "密码错误"
                  });
                } else if (res.data.status == 400) {
                  this.$message({
                    type: 'error',
                    message: "账号未注册"
                  });
                } else if (res.data.status == 500) {
                  this.$message({
                    type: 'error',
                    message: "非POST请求"
                  });
                }
              })
            } else {
              console.log('error!!');
              return false;
            }
          });
        },
        resetForm(formName) {
          this.$refs[formName].resetFields();
        }
      }
    }
</script>

<style scoped>
    #building{
      background:url("@/assets/images/pexels-jess-bailey-designs-1558691.jpg");
      background-size: cover;
      width:100%;
      height:100%;
      position:fixed;
      background-position: center center;
    }
    .head {
        margin-left: 100px;
    }
    .login-box {
        height: 600px;
        display:flex;
        justify-content:center;
        align-items: center;
    }
    .box-card {
      background-color: rgba(255,255,255,0.6);
      border-radius: 20px;
      width: 400px;
    }
    .card {
        height: 500px;
        display:flex;
        justify-content:center;
        align-items: center;
    }
    .button1 {
        margin-left: 30px;
    }
</style>