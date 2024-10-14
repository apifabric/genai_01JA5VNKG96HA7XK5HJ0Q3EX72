import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InventoryItemHomeComponent } from './home/InventoryItem-home.component';
import { InventoryItemNewComponent } from './new/InventoryItem-new.component';
import { InventoryItemDetailComponent } from './detail/InventoryItem-detail.component';

const routes: Routes = [
  {path: '', component: InventoryItemHomeComponent},
  { path: 'new', component: InventoryItemNewComponent },
  { path: ':id', component: InventoryItemDetailComponent,
    data: {
      oPermission: {
        permissionId: 'InventoryItem-detail-permissions'
      }
    }
  }
];

export const INVENTORYITEM_MODULE_DECLARATIONS = [
    InventoryItemHomeComponent,
    InventoryItemNewComponent,
    InventoryItemDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class InventoryItemRoutingModule { }