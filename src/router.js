// 配置路由相关的信息
import VueRouter from 'vue-router'
import Vue from 'vue'

import CheckApplyForProject from './views/apply/CheckApplyForProject'
import CheckApplyForTeamManager from './views/apply/CheckApplyForTeamManager'
import CheckApplyForTeamMember from './views/apply/CheckApplyForTeamMember'

import CreateProject from './views/project/CreateProject'
import ProjectInfoPage from './views/project/ProjectInfoPage'

import UserProjectArea from './views/home/UserProjectArea'
import ManageTeam from './views/home/ManageTeam'
import CheckCreateProjectApply from './views/home/CheckCreateProjectApply'

import MessageArea from './views/message/MessageArea'
import SendMessage from './views/message/SendMessage'

import CreateTeam from './views/team/CreateTeam'
import UserTeamArea from './views/team/UserTeamArea'
import TeamInfoPage from './views/team/TeamInfoPage'
import CheckCreatTeamApply from './views/team/CheckCreatTeamApply'

import RegisterPage from './views/welcome/RegisterPage'
import LogIn from './views/welcome/LogIn'

import UserInfoPage from './views/user/UserInfoPage'
import UserJoinedProjects from './views/user/UserJoinedProjects'
import UserJoinedTeams from './views/user/UserJoinedTeams'
 
// 1.通过Vue.use(插件), 安装插件
Vue.use(VueRouter)

// 解决 ElementUI 导航栏中的 vue-router 在3.0版本以上重复点菜单报错问题
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}
 
// 2.创建VueRouter对象
const routes = [
  {
    path: '',
    // redirect重定向
    redirect: '/Login/'
  },
  {
    path: '/Login/',
    component: LogIn
  },
  {
    path: '/register/',
    component: RegisterPage
  },
  {
    path: '/home',
    component: UserProjectArea
  },
  {
    path: '/ManageTeam',
    component: ManageTeam
  },
  {
    path: '/CheckCreateProjectApply',
    component: CheckCreateProjectApply
  },
  {
    path: '/user_page/',
    component: UserInfoPage
  },
  {
    path: '/CreateProject/',
    component: CreateProject
  },
  {
    path: '/CreateTeam',
    component: CreateTeam
  },
  {
    path: '/CheckCreateTeamApply',
    component: CheckCreatTeamApply
  },
  {
    path: '/check_message/',
    component: MessageArea
  },
  {
    path: '/project/:id',
    component: ProjectInfoPage
  },
  {
    path: '/joined_project/',
    component: UserJoinedProjects
  },
  {
    path: '/joined_team/',
    component: UserJoinedTeams
  },
  {
    path: '/team_home/',
    component: UserTeamArea
  },
  {
    path: '/team/:id',
    component: TeamInfoPage
  },
  {
    path: '/check_apply',
    component: CheckApplyForProject
  },
  {
    path: '/check_apply_manager/',
    component: CheckApplyForTeamManager
  },
  {
    path: '/check_apply_member/',
    component: CheckApplyForTeamMember
  },
  {
    path: '/new_message/',
    component: SendMessage
  }
]
const router = new VueRouter({
  // 配置路由和组件之间的应用关系
  routes,
  mode: 'history',
  linkActiveClass: 'active'
})
 
// 3.将router对象传入到Vue实例
export default router
 