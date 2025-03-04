import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SupplierHomeComponent } from './home/Supplier-home.component';
import { SupplierNewComponent } from './new/Supplier-new.component';
import { SupplierDetailComponent } from './detail/Supplier-detail.component';

const routes: Routes = [
  {path: '', component: SupplierHomeComponent},
  { path: 'new', component: SupplierNewComponent },
  { path: ':id', component: SupplierDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Supplier-detail-permissions'
      }
    }
  },{
    path: ':supplier_id/InventoryItem', loadChildren: () => import('../InventoryItem/InventoryItem.module').then(m => m.InventoryItemModule),
    data: {
        oPermission: {
            permissionId: 'InventoryItem-detail-permissions'
        }
    }
},{
    path: ':supplier_id/PurchaseOrder', loadChildren: () => import('../PurchaseOrder/PurchaseOrder.module').then(m => m.PurchaseOrderModule),
    data: {
        oPermission: {
            permissionId: 'PurchaseOrder-detail-permissions'
        }
    }
}
];

export const SUPPLIER_MODULE_DECLARATIONS = [
    SupplierHomeComponent,
    SupplierNewComponent,
    SupplierDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SupplierRoutingModule { }