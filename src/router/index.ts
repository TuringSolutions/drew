import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/aboutus",
    name: "About Us",
    component: () => import("../views/AboutUs.vue")
  },
  {
    path: "/services/softwaredev",
    name: "Software Development",
    component: () => import("../views/services/SoftwareDevelopment.vue")
  },
  {
    path: "/services/computervision",
    name: "Computer Vision",
    component: () => import("../views/services/ComputerVision.vue")
  }
];

const router = createRouter({
  routes: routes,
  history: createWebHistory(),
});

export default router;
