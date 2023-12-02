<!--包含加入团体申请，以及加入项目申请-->
<template>
	<div>
		<managerHomeHeader></managerHomeHeader>
		<div>
			<el-col span="4" class="sideMenu">
				<el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
				<el-menu-item index="1">
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
				<div>
					<el-button @click="change()">切换</el-button>
				</div>
				<!--加入-->
				<el-table :data="in_applies" border v-show="this.isIn">
					<el-table-column prop="student_name" label="申请人姓名" width="150"></el-table-column>
					<el-table-column prop="project_name" label="申请加入项目" width="250"></el-table-column>
					<el-table-column label="查看详情" width="350">
						<template slot-scope="scope">
							<el-button @click="getStudentInfo(scope.row.student_id)" type="text">查看申请人信息</el-button>
							<el-button @click="getProjectInfo(scope.row.project_id)" type="text">查看项目详情</el-button>
						</template>
					</el-table-column>
					<el-table-column label="审核申请" width="200">
						<template slot-scope="scope">
							<el-button @click="dealApply_in(scope.row.student_id, scope.row.project_id)" type="text">审核</el-button>
						</template>
					</el-table-column>
				</el-table>
				<!--退出-->
				<el-table :data="out_applies" border v-show="this.isOut">
					<el-table-column prop="student_name" label="申请人姓名" width="150"></el-table-column>
					<el-table-column prop="project_name" label="申请退出项目" width="250"></el-table-column>
					<el-table-column label="查看详情" width="350">
						<template slot-scope="scope">
							<el-button @click="getStudentInfo(scope.row.student_id)" type="text">查看申请人信息</el-button>
							<el-button @click="getProjectInfo(scope.row.project_id)" type="text">查看项目详情</el-button>
						</template>
					</el-table-column>
					<el-table-column label="审核申请" width="200">
						<template slot-scope="scope">
							<el-button @click="dealApply_out(scope.row.student_id, scope.row.project_id)" type="text">审核</el-button>
						</template>
					</el-table-column>
				</el-table>
			</el-col>
		</div>
		<!--审核加入结果dialog-->
		<div>
			<el-dialog title="审核结果反馈" :visible.sync="resultDialogVisible_in">
				<el-form :model="form" label-width="80px">
					<el-form-item label="审核结果">
						<el-radio-group v-model="form.result">
							<el-radio label="通过"></el-radio>
							<el-radio label="拒绝"></el-radio>
						</el-radio-group>
					</el-form-item>
					<el-form-item label="原因">
						<el-input v-model="form.reason"></el-input>
					</el-form-item>
					<el-form-item>
						<div>
							<el-button @click="submitForm_in()">提交</el-button>
							<el-button @click="resultDialogVisible_in = flase">取消</el-button>
						</div>
					</el-form-item>
				</el-form>
			</el-dialog>
		</div>
		<!--审核退出结果dialog-->
		<div>
			<el-dialog title="审核结果反馈" :visible.sync="resultDialogVisible_out">
				<el-form :model="form" label-width="80px">
					<el-form-item label="审核结果">
						<el-radio-group v-model="form.result">
							<el-radio label="通过"></el-radio>
							<el-radio label="拒绝"></el-radio>
						</el-radio-group>
					</el-form-item>
					<el-form-item label="原因">
						<el-input v-model="form.reason"></el-input>
					</el-form-item>
					<el-form-item>
						<div>
							<el-button @click="submitForm_out()">提交</el-button>
							<el-button @click="resultDialogVisible_out = flase">取消</el-button>
						</div>
					</el-form-item>
				</el-form>
			</el-dialog>
		</div>
		<!--个人信息dialog-->
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
	async created() {
		await this.axios({
			method: 'post',
			url: 'http://localhost:8000/buaa_db/man_get_stu_in_project/',
			headers: {'Content-Type': 'multipart/form-data'},
			}).then((res)=>{
			this.in_applies = res.data.applies
		})
		await this.axios({
			method: 'post',
			url: 'http://localhost:8000/buaa_db/man_get_stu_out_project/',
			headers: {'Content-Type': 'multipart/form-data'},
		}).then((res)=>{
			this.out_applies = res.data.applies
		})
	},
	data() {
		return {
			in_applies: [
				{student_id: '1' ,student_name: '张三', project_id: '1', project_name: '项目一'},
				{student_id: '1' ,student_name: '张三', project_id: '1', project_name: '项目一'},
				{student_id: '1' ,student_name: '张三', project_id: '1', project_name: '项目一'},
			],
			out_applies: [
				{student_id: '1' ,student_name: '李四', project_id: '1', project_name: 'xxx项目'},
				{student_id: '1' ,student_name: '李四', project_id: '1', project_name: 'xxx项目'},
				{student_id: '1' ,student_name: '李四', project_id: '1', project_name: 'xxx项目'},
			],
			student_info: {
				name: '张三', student_id: '21370000', phone_num: '18000000000'
			},
			studentdialogVisible: false,
			resultDialogVisible_in: false,
			resultDialogVisible_out: false,
			isIn: true,
			isOut: false,
			form: {
				result: '',
				reason: ''
			},
			deal_student_id: '',
			deal_project_id: ''
		}
	},
	methods: {
		change() {
			this.isIn = !this.isIn,
			this.isOut = !this.isOut
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
		getProjectInfo(project_id) {
			this.$router.push('/project/' + project_id);
		},
		dealApply_in(student_id, project_id) {
			this.deal_student_id = student_id,
			this.deal_project_id = project_id,
			this.resultDialogVisible_in = true
		},
		dealApply_out(student_id, project_id) {
			this.deal_student_id = student_id,
			this.deal_project_id = project_id,
			this.resultDialogVisible_out = true
		},
		submitForm_in() {
			this.axios({
				method: 'post',
				url: 'http://localhost:8000/buaa_db/man_check_stu_project_in/',
				headers: {'Content-Type': 'multipart/form-data'},
				data: {
					'receiver_id': this.deal_student_id,
					'project_id': this.deal_project_id,
					'result': this.form.result,
					'reason': this.form.reason
				}
			}).then((res)=>{
				if (res.data.status == 200) {
					this.$message({
						message: '审核结果已发送',
						type: 'success'
					})
				}
			})
		},
		submitForm_out() {
			this.axios({
				method: 'post',
				url: 'http://localhost:8000/buaa_db/man_check_stu_project_out/',
				headers: {'Content-Type': 'multipart/form-data'},
				data: {
					'receiver_id': this.deal_student_id,
					'project_id': this.deal_project_id,
					'result': this.form.result,
					'reason': this.form.reason
				}
			}).then((res)=>{
				if (res.data.status == 200) {
					this.$message({
						message: '审核结果已发送',
						type: 'success'
					})
				}
			})
		}
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