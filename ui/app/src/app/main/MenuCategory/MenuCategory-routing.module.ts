import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MenuCategoryHomeComponent } from './home/MenuCategory-home.component';
import { MenuCategoryNewComponent } from './new/MenuCategory-new.component';
import { MenuCategoryDetailComponent } from './detail/MenuCategory-detail.component';

const routes: Routes = [
  {path: '', component: MenuCategoryHomeComponent},
  { path: 'new', component: MenuCategoryNewComponent },
  { path: ':id', component: MenuCategoryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'MenuCategory-detail-permissions'
      }
    }
  },{
    path: ':category_id/MenuItem', loadChildren: () => import('../MenuItem/MenuItem.module').then(m => m.MenuItemModule),
    data: {
        oPermission: {
            permissionId: 'MenuItem-detail-permissions'
        }
    }
}
];

export const MENUCATEGORY_MODULE_DECLARATIONS = [
    MenuCategoryHomeComponent,
    MenuCategoryNewComponent,
    MenuCategoryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MenuCategoryRoutingModule { }