<template>
  <div>
    <managerHomeHeader></managerHomeHeader>
    <div class="list">
      <!--v-loading?-->
      <el-row :gutter="30" style="margin-right: 15px;margin-left: -5px" type="flex" v-loading="loading">
      <el-col v-for="(item, index) in teams" :key="index" class="item" :span="8">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>{{ item.name }}</span>
          </div>
          <div class="text item">{{ item.time }}</div>
          <div class="text item">{{ item.description }}</div>
          <el-divider></el-divider>
          <el-button @click="viewTeam(item.id)" type="text">查看详情</el-button>
          <el-button @click="getProjects(item.id)" type="text">管理团队项目</el-button>
          <el-button @click="getMember(item.id)" type="text">查看成员</el-button>
          <!--对话框-->
          <el-dialog title="团队项目" :visible.sync="projectDialogVisible">
            <el-table :data="projects" height="250">
              <el-table-column property="name" label="项目名称" width="200"></el-table-column>
              <el-table-column property="time" label="时间" width="150"></el-table-column>
              <el-table-column property="position" label="地点" width="150"></el-table-column>
              <el-table-column label="操作" width="300">
                <template slot-scope="scope">
                  <el-button @click="getProjectInfo(scope.row.id)" size="small">查看项目详情</el-button>
                  <el-button @click="deleteProject(scope.row.id)" type="danger" size="small">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
            <el-dialog width="30%" title="删除确认" :visible.sync="deleteVisible" append-to-body>
              <span>您确认要删除该项目吗</span>
              <span slot="footer" class="dialog-footer">
                <el-button @click="deleteVisible = false">取 消</el-button>
                <el-button type="primary" @click="innerDeleteProject()">确 定</el-button>
              </span>
            </el-dialog>
          </el-dialog>
          <el-dialog title="团队成员" :visible.sync="memberDialogVisible">
            <el-table :data="students" height="250">
              <el-table-column property="id" label="学工号" width="150"></el-table-column>
              <el-table-column property="name" label="姓名" width="100"></el-table-column>
              <el-table-column label="操作" width="300">
                <template slot-scope="scope">
                  <el-button @click="viewMemberInfo(scope.row.id)" type="text">查看成员详情</el-button>
                  </template>
              </el-table-column>
            </el-table>
          </el-dialog>
        </el-card>
      </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import managerHomeHeader from "@/components/managerHomeHeader/"
export default {
  components: {managerHomeHeader},
  async created() {
    await this.axios({
      method: 'post',
      url: 'http://localhost:8000/buaa_db/get_manage_teams/',
      headers: {'Content-Type': 'multipart/form-data'},
    }).then((res)=>{
      this.teams = res.data.teams;
    })
  },
  data() {
    return {
      teams : [
        {id:1, name:"团体一", time:"2023-10-18", description: "..."},
        {id:2, name:"团体二", time:"2023-10-21", description: "..."},
        {id:3, name:"团体一", time:"2023-10-18", description: "..."},
        {id:4, name:"团体二", time:"2023-10-21", description: "..."},
        {id:5, name:"团体一", time:"2023-10-18", description: "..."},
        {id:6, name:"团体二", time:"2023-10-21", description: "..."},
        {id:7, name:"团体一", time:"2023-10-18", description: "..."},
        {id:8, name:"团体二", time:"2023-10-21", description: "..."},
      ],
      students:[
        {id:1,name: '王小虎'},
        {id:2,name: '王小虎'},
        {id:3,name: '王小虎'},
        {id:4,name: '王小虎'},
      ],
      projects: [
        {id: '1', name: 'xxx项目', time: '2023-11-17', position: 'posxxx', description:'xxxxxxxx'},
        {id: '2', name: 'xxx项目', time: '2023-11-17', position: 'posxxx', description:'xxxxxxxx'},
        {id: '3', name: 'xxx项目', time: '2023-11-17', position: 'posxxx', description:'xxxxxxxx'},
        {id: '4', name: 'xxx项目', time: '2023-11-17', position: 'posxxx', description:'xxxxxxxx'},
      ],
      memberDialogVisible: false,
      projectDialogVisible: false,
      deleteVisible: false,
      deleteProjectId: '',
    }
  },
  methods: {
    viewTeam(id) {
      this.$router.push({
        path: '/team/' + id
      })
    },
    getMember(id) {
      this.axios({
        method: 'post',
        url: 'http://localhost:8000/buaa_db/get_team_students/',
        headers: {'Content-Type': 'multipart/form-data'},
        data: {
          'team_id': id
        }
      }).then((res)=>{
        this.students = res.data.students;
      })
      this.memberDialogVisible = true;
    },
    getProjects(id) {
      this.axios({
        method: 'post',
        url: 'http://localhost:8000/buaa_db/get_team_projects/',
        headers: {'Content-Type': 'multipart/form-data'},
        data: {
          'team_id': id
        }
      }).then((res)=>{
        this.projects = res.data.projects;
      })
      this.projectDialogVisible = true;
    },
    getProjectInfo(id) {
      this.$router.push('/project/' + id);
    },
    deleteProject(id) {
      this.deleteVisible = true;
      this.deleteProjectId = id;
    },
    innerDeleteProject() {
      console.log(this.deleteProjectId);
      this.axios({
        method: 'post',
        url: 'http://localhost:8000/buaa_db/man_delete_project/',
        headers: {'Content-Type': 'multipart/form-data'},
        data: {
          'id': this.deleteProjectId
        }
      }).then((res)=>{
        if (res.data.status == 200) {
          this.$message({
            type: 'success',
            message: '删除项目成功'
          })
        }
        else {
          this.$message.error('删除项目失败')
        }
      })
      this.deleteVisible = false;
    },
    downloadFile(fileName) {
      const fileUrl = '/path/to/' + fileName; // 文件的URL地址
      window.open(fileUrl);
    },
    viewMemberInfo(id) {
      id;
    }
  }
}
</script>

<style scoped>
  .list {
    margin-left: 120px;
    margin-right: 120px;
  }
  .item {
    padding: 0px;
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
    margin-top: 20px;
    transition: all .5s;
  }
  .el-form-item {
    margin-bottom: 0 !important;
  }
</style>