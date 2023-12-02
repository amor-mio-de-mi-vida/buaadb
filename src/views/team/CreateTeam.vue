<template>
    <div>
      <div>
        <managerHomeHeader></managerHomeHeader>
      </div>
      <div class="content">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="团体名称">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="团体描述">
            <el-input type="textarea" v-model="form.profile" :rows="10"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">立即创建</el-button>
            <el-button @click="back">取消</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
</template>

<script>
  import managerHomeHeader from "@/components/managerHomeHeader";
    export default {
      components: {managerHomeHeader},
      data() {
        return {
            form: {
                name: '',
                profile: '',
                image: ''
            },
            dynamicTags: [],
            inputVisible: false,
            inputValue: ''
        };
      },
      methods: {
        onSubmit() {
          console.log(this.form)
          this.axios({
            method: 'post',
            credentials: 'include',
            url: 'http://localhost:8000/buaa_db/man_create_team/',
            headers: {'Content-Type': 'multipart/form-data'},
            data: this.form
          }).then((res) => {
            console.log(res);
            if (res.data.status == 200) { //后端传回数据
              this.$message({
                type: 'success',
                message: "创建团队成功"
              });
              this.$router.push({
                path: '/ManageTeam/'
              })
            }
            else if (res.data.status == 400) {
              this.$message.error('团队名称重复');
            }
            else {
              this.$message.error('创建团队失败');
            }
          })
        },

        handleClose(tag) {
          this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
        },
  
        showInput() {
          this.inputVisible = true;
          // eslint-disable-next-line
          this.$nextTick(_ => {
            this.$refs.saveTagInput.$refs.input.focus();
          });
        },
  
        handleInputConfirm() {
          let inputValue = this.inputValue;
          if (inputValue) {
            this.dynamicTags.push(inputValue);
          }
          this.inputVisible = false;
          this.inputValue = '';
        },

        back() {
          this.$router.push({
            path: '/ManageTeam/'
          })
        }
      }
    }
  </script>

<style>
  .content {
    margin-left: 120px;
    margin-right: 500px;
    margin-top: 20px;
  }
  .center {
      text-align: center;
  }
  .el-tag + .el-tag {
      margin-left: 10px;
  }
  .button-new-tag {
      margin-left: 10px;
      height: 32px;
      line-height: 30px;
      padding-top: 0;
      padding-bottom: 0;
  }
  .input-new-tag {
      width: 90px;
      margin-left: 10px;
      vertical-align: bottom;
  }
</style>