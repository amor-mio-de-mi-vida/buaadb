<template>
    <div id="building">
        <div class="head">
            <router-link :to="'/login'" style="text-decoration: none;">
                <h1>Home</h1>
            </router-link>
        </div>
        <div class="registerCard">
          <el-card class="box-card">
            <el-form :model="form" :rules="rules" ref="form" label-width="100px" class="register-form">
                <el-form-item label="学号" prop="id">
                    <el-col >
                        <el-input v-model="form.id" autocomplete="off"></el-input>
                    </el-col>
                </el-form-item>
                <el-form-item label="用户名" prop="name">
                    <el-col >
                        <el-input v-model="form.name" autocomplete="off"></el-input>
                    </el-col>
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
                <el-form-item label="密码" prop="password">
                    <el-col>
                        <el-input type="password" v-model="form.password" autocomplete="off"></el-input>
                    </el-col>
                </el-form-item>
                <el-form-item label="确认密码" prop="password_again">
                    <el-col>
                        <el-input type="password" v-model="form.password_again" autocomplete="off"></el-input>
                    </el-col>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="submitForm('form')">提交</el-button>
                    <el-button @click="resetForm('form')">重置</el-button>
                </el-form-item>
            </el-form>
          </el-card>
        </div>
    </div>
    
</template>

<script>
    export default {
      data() {
        /*var validatePass = (rule, value, callback) => {
          if (value === '') {
            callback(new Error('请输入密码'));
          } else {
            if (this.form.checkPass !== '') {
              this.$refs.form.validateField('checkPass');
            }
            callback();
          }
        };
        var validatePass2 = (rule, value, callback) => {
          if (value === '') {
            callback(new Error('请再次输入密码'));
          } else if (value !== this.form.pass) {
            callback(new Error('两次输入密码不一致!'));
          } else {
            callback();
          }
        };*/
        return {
          form: {
            id: '',
            password: '',
            password_again: '',
            role: '',
            name: ''
          },
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
          rules: {
            id: [
                { required: true, message: '请输入学工号', trigger: 'blur' },
            ],
            role: [
                { required: true, message: '请选择注册身份', trigger: 'blur' },
            ],
            name: [
                { required: true, message: '请输入用户名', trigger: 'blur' },
            ],
            password: [
                { required: true, message: '请输入密码', trigger: 'blur' },
                //{ required: true, validator: validatePass, trigger: 'blur' }
            ],
            password_again: [
                { required: true, message: '请再次输入密码', trigger: 'blur' },
                //{ required: true, validator: validatePass2, trigger: 'blur' }
            ],
          }
        };
      },
      methods: {
        submitForm(formName) {
          let data = {
            id: this.form.id,
            name: this.form.name,
            password: this.form.password,
            password_again: this.form.password_again,
            role: this.form.role,
          }
          console.log(data);
          this.$refs[formName].validate((valid) => {
            if (valid) {
              this.axios({
                method: 'post',
                url: 'http://localhost:8000/buaa_db/register/',
                headers: {'Content-Type': 'multipart/form-data'},
                data: data
              }).then((res) => {
                console.log("1"); //调试
                if (res.data.status === 200) {
                  this.$message({
                    type: 'success',
                    message: "创建成功"
                  });
                  this.$router.push({path: '/login/'}) // check
                } else if (res.data.status == 401) {
                  this.$message({
                    type: 'error',
                    message: "无注册权限，学工号不合法"
                  });
                } else if (res.data.status == 402) {
                  this.$message({
                    type: 'error',
                    message: "学号已被注册"
                  });
                } else if (res.data.status == 404) {
                  this.$message({
                    type: 'error',
                    message: "两次密码不一致"
                  });
                } else if (res.data.status == 500) {
                  this.$message({
                    type: 'error',
                    message: "非POST请求"
                  });
                }
              })
            } else {
              console.log('error submit!!');
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
    .box-card {
      background-color: rgba(255,255,255,0.6);
      border-radius: 20px;
      width: 400px;
    }
    .register-form {
      margin: 20px 20px 20px 0px
    }
    .head {
        margin-left: 100px;
    }
    .registerCard {
        height: 550px;
        display:flex;
        justify-content:center;
        align-items: center;
    }
</style>