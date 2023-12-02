<template>
	<div>
		<sysManagerHomeHeader></sysManagerHomeHeader>
		<!--系统管理员处理创建项目申请-->
		<div class="team_table">
			<el-table :data="projects" border style="width: 100%" height="600">
			<el-table-column fixed prop="name" label="项目名称" width="150"></el-table-column>
			<el-table-column fixed prop="time_start" label="起始时间" width="200"></el-table-column>
			<el-table-column fixed prop="time_end" label="结束时间" width="200"></el-table-column>
			<el-table-column fixed prop="location" label="地点" width="150"></el-table-column>
			<el-table-column fixed prop="time" label="提交申请时间" width="200"></el-table-column>
			<el-table-column fixed="right" label="操作" width="200">
				<template slot-scope="scope">
				<!--scope.row可以获取当前行的信息-->
				<el-button @click="viewProject(scope.row.id)" type="text">查看详情</el-button>
				<el-button @click="dealApply(scope.row.id)" type="text">处理申请</el-button>
				</template>
			</el-table-column>
			</el-table>
		</div>
		<!--审核结果dialog-->
		<div>
			<el-dialog title="审核结果反馈" :visible.sync="resultDialogVisible">
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
							<el-button @click="submitForm()">提交</el-button>
							<el-button @click="resultDialogVisible = flase">取消</el-button>
						</div>
					</el-form-item>
				</el-form>
			</el-dialog>
		</div>
	</div>
</template>

<script>
import sysManagerHomeHeader from "@/components/sysManagerHomeHeader/"
export default {
	components: {sysManagerHomeHeader},
	async created() {
		await this.axios({
			method: 'post',
			url: 'http://localhost:8000/buaa_db/admin_get_apply_project/',
			headers: {'Content-Type': 'multipart/form-data'},
		}).then((res)=>{
			console.log(res)
			this.projects = res.data.projects;
		})
	},
	data() {
		return {
			resultDialogVisible: false,
			/*projects : [
				{id:1, name:"活动一",location:"操场", time_start:"2023-10-18", time_end: '2023-10-19'},
				{id:1, name:"活动一",location:"操场", time_start:"2023-10-18", time_end: '2023-10-19'},
				{id:1, name:"活动一",location:"操场", time_start:"2023-10-18", time_end: '2023-10-19'},
				{id:1, name:"活动一",location:"操场", time_start:"2023-10-18", time_end: '2023-10-19'},
				{id:1, name:"活动一",location:"操场", time_start:"2023-10-18", time_end: '2023-10-19'},
				{id:1, name:"活动一",location:"操场", time_start:"2023-10-18", time_end: '2023-10-19'},
			],*/
			projects: [],
			form: {project_id: '', result: '', reason:''}
		}
	},
	methods: {
		viewProject(id) {
			this.$router.push({
				path: '/project/' + id
			})
		},
		dealApply(id) {
			this.resultDialogVisible = true;
			this.form.project_id = id;
		},
		submitForm() {
			this.axios({
				method: 'post',
				url: 'http://localhost:8000/buaa_db/admin_check_apply_project/',
				headers: {'Content-Type': 'multipart/form-data'},
				data: this.form
			}).then((res)=>{
				if (res.data.status == 200) {
					this.$message({
						message: '审核提交成功'
					})
				}
				else {
					this.$message.error('审核提交失败')
				}
			})
		},
	}
}
</script>

<style scoped>
	.el-card {
		width: 100%;
	}
	.list {
		margin-right: 120px;
	}
	.team_table {
		margin-top: 20px;
		margin-left: 120px;
		margin-right: 120px;
	}
</style>