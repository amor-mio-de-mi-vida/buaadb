<template>
    <div class="uploaderBase">
      <input multiple
             type="file"
             autocomplete="off"
             tabindex="-1"
             id="upload"
             accept=".pdf,.word,.rar,.zip"
             @change="handleFile($event)"
             style="display: none;"/>
      <div class="submitInfo">
        <!--icon-->
        <div class="icon"><i class="el-icon-paperclip"></i></div>
        <!--input line-->
        <div class="input" onclick="document.querySelector('#upload').click()">
          <span class="inputFont">选择文件</span>
        </div>
        <!--uploader btn-->
        <div>
          <el-button class="fontUp" type="text" @click="upload()"><i class="el-icon-upload"></i> 提交</el-button>
        </div>
      </div>
      <div slot="tip" class="el-upload__tip">只能上传pdf文件，多个文件请压缩成rar/zip压缩包</div>
      <div class="preview">
        <div v-for="(file, index) in this.files" :myIndex="index" :key="file.name" class="uploadSuccess">
            <el-col span="20">
                <div><i class="el-icon-document-checked" style="margin: 5px;"></i>{{ file.name }}</div>
            </el-col>
            <el-button @click="deleteFile($event)" class="deleteBtn" type="text warning" icon="el-icon-circle-close">
                <i class="el-circle-close"></i>
            </el-button>
        </div>
      </div>
    </div>
  </template>
  
<script>
export default {
    name: "upLoader",
    props: ['project_id', 'lastSubmit'],
    data() {
        return {
            files: []
        }
    },
    methods: {
        handleFile(event) {
            const file = event.target.files[0];
            this.files.splice(0, 1);
            this.files.push(file);
            // eslint-disable-next-line vue/no-mutating-props
            this.lastSubmit = file.name;
        },
        deleteFile(e) {
            const index = e.currentTarget.parentElement.getAttribute('myIndex');
            const name = this.files[index].name;
            this.$confirm('此操作将删除该文件, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                this.files.splice(index, 1);
                this.$message({
                    type: 'success',
                    message: '删除: ' + name
                });
            }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });
            });
            },
        upload() {
            var formData = new FormData();
            if (this.files.length === 0) {
                this.$message({
                    message: '上传文件列表为空！',
                    type: 'error'
                })
            } 
            else {
                formData.append('hw_submit', this.files[0]); // 仅有一个文件
                formData.append('id', this.project_id);
                console.log(formData.get('hw_submit'));
                this.$axios({
                    method: 'post',
                    url: 'http://localhost:8000/buaa_db/stu_pub_feedback/',
                    data: formData,   // 发现 data 后面直接跟 formData 后端才能接收到
                    headers: {
                        token: this.$store.getters.getToken //todo
                    }
                }).then(res => {
                    if (res.data.value === 200) {
                        this.$message({
                            message: '上传成功',
                            type: 'success'
                        })
                    } else {
                        this.$message({
                            message: '上传失败',
                            type: 'error'
                        })
                    }
                })
                }
        },
    },
    mounted() {
        if(this.lastSubmit) {
            this.files = [{name: this.lastSubmit}]
        } else {
            this.files = []
        }
    }
}
</script>