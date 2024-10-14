import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TableHomeComponent } from './home/Table-home.component';
import { TableNewComponent } from './new/Table-new.component';
import { TableDetailComponent } from './detail/Table-detail.component';

const routes: Routes = [
  {path: '', component: TableHomeComponent},
  { path: 'new', component: TableNewComponent },
  { path: ':id', component: TableDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Table-detail-permissions'
      }
    }
  },{
    path: ':table_id/Order', loadChildren: () => import('../Order/Order.module').then(m => m.OrderModule),
    data: {
        oPermission: {
            permissionId: 'Order-detail-permissions'
        }
    }
},{
    path: ':table_id/Reservation', loadChildren: () => import('../Reservation/Reservation.module').then(m => m.ReservationModule),
    data: {
        oPermission: {
            permissionId: 'Reservation-detail-permissions'
        }
    }
}
];

export const TABLE_MODULE_DECLARATIONS = [
    TableHomeComponent,
    TableNewComponent,
    TableDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TableRoutingModule { }