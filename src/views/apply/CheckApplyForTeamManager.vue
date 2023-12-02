<!--包含加入团体申请，以及加入项目申请-->
<template>
	<div>
		<managerHomeHeader></managerHomeHeader>
		<div>
			<el-col span="4" class="sideMenu">
				<el-menu default-active="2-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
				<el-menu-item index="1" @click="check_apply_project()">
					<i class="el-icon-menu"></i>
					<span slot="title">项目申请</span>
				</el-menu-item>
				<el-submenu index="2">
					<template slot="title">
					<i class="el-icon-location"></i>
					<span>团队申请</span>
					</template>
					<el-menu-item-group>
					<el-menu-item index="2-1" @click="check_apply_manager()">团队管理员申请</el-menu-item>
					<el-menu-item index="2-2" @click="check_apply_member()">团队参与者申请</el-menu-item>
					</el-menu-item-group>
				</el-submenu>
				</el-menu>
			</el-col>
			<el-col span="18" class="project_apply_table" style="width:65%">
				<el-table :data="team_manager_applies" border>
					<el-table-column prop="name" label="申请人姓名" width="150"></el-table-column>
					<el-table-column prop="team_name" label="申请管理团队" width="250"></el-table-column>
					<el-table-column prop="type" label="类别" width="100">
						<template slot-scope="scope">
							<el-tag :type="getType(scope.row.type)">{{scope.row.type}}</el-tag>
						</template>
					</el-table-column>
					<el-table-column label="查看详情" width="350">
						<template slot-scope="scope">
							<el-button @click="getStudentInfo(scope.row.student_id)" type="text">查看申请人信息</el-button>
							<el-button @click="getProjectInfo(scope.row.team_id)" type="text">查看团队详情</el-button>
						</template>
					</el-table-column>
					<el-table-column label="审核申请" width="200">
						<template slot-scope="scope">
							<el-button @click="passApply(scope.row.student_id, scope.row.team_id)" type="text">通过</el-button>
							<el-button @click="refuseApply(scope.row.student_id, scope.row.team_id)" type="text">拒绝</el-button>
						</template>
					</el-table-column>
				</el-table>
			</el-col>
		</div>
		<div>
			<el-dialog title="申请人信息" :visible.sync="studentdialogVisible">
				<el-descriptions>
					<el-descriptions-item label="用户名">{{this.student_info.name}}</el-descriptions-item>
					<el-descriptions-item label="学号">{{this.student_info.student_id}}</el-descriptions-item>
					<el-descriptions-item label="电话号码">{{this.student_info.phone_num}}</el-descriptions-item>
				</el-descriptions>
			</el-dialog>
		</div>
	</div>
</template>

<script>
import managerHomeHeader from "@/components/managerHomeHeader"
export default {
	components: {managerHomeHeader},
	data() {
		return {
			team_manager_applies: [
				{student_id: '1' ,name: '张三', team_id: '1', team_name: 'xxx志愿团体', type: '加入'},
				{student_id: '1' ,name: '张三', team_id: '1', team_name: 'xxx志愿团体', type: '加入'},
				{student_id: '1' ,name: '张三', team_id: '1', team_name: 'xxx志愿团体', type: '退出'},
				{student_id: '1' ,name: '张三', team_id: '1', team_name: 'xxx志愿团体', type: '退出'},
			],
			student_info: {
				name: '张三', student_id: '21370000', phone_num: '18000000000'
			},
			studentdialogVisible: false,
		}
	},
	methods: {
		check_apply_project() {
			this.$router.push('/check_apply/');
		},
		check_apply_manager() {
			this.$router.push('/check_apply_manager/');
		},
		check_apply_member() {
			this.$router.push('/check_apply_member/');
		},
		getType(type) {
			if (type == '加入') {
				return 'success';
			}
			else {
				return 'danger';
			}
		},
		getStudentInfo(student_id) {
			this.axios({
				method: 'post',
				url: '',
				param: student_id
			}).then((res)=>{
				this.student_info = res.data.student_info
			})
			this.studentdialogVisible = true;
		},
		getProjectInfo(team_id) {
			this.$router.push('/project/' + team_id);
		},
		passApply(student_id, team_id) {
			this.axios({
				method: 'post',
				url: '',
				data: {student_id, team_id}
			}).then((res)=>{
				if (res.data.status == 200) {
					this.$message({
						type: 'success',
						message: "成功通过申请"
					})
				}
			})
		},
		refuseApply(student_id, team_id) {
			this.axios({
				method: 'post',
				url: '',
				data: {student_id, team_id}
			}).then((res)=>{
				if (res.data.status == 200) {
					this.$message({
						type: 'success',
						message: "成功拒绝申请"
					})
				}
			})
		},

	}
}
</script>

<style scoped>
	.sideMenu {
		margin-left: 120px;
	}
	.el-project_apply_table {
		margin-right: 120px;
	}
</style>