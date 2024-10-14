import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Customer', loadChildren: () => import('./Customer/Customer.module').then(m => m.CustomerModule) },
    
        { path: 'Employee', loadChildren: () => import('./Employee/Employee.module').then(m => m.EmployeeModule) },
    
        { path: 'InventoryItem', loadChildren: () => import('./InventoryItem/InventoryItem.module').then(m => m.InventoryItemModule) },
    
        { path: 'MenuCategory', loadChildren: () => import('./MenuCategory/MenuCategory.module').then(m => m.MenuCategoryModule) },
    
        { path: 'MenuItem', loadChildren: () => import('./MenuItem/MenuItem.module').then(m => m.MenuItemModule) },
    
        { path: 'Order', loadChildren: () => import('./Order/Order.module').then(m => m.OrderModule) },
    
        { path: 'OrderItem', loadChildren: () => import('./OrderItem/OrderItem.module').then(m => m.OrderItemModule) },
    
        { path: 'Payment', loadChildren: () => import('./Payment/Payment.module').then(m => m.PaymentModule) },
    
        { path: 'PurchaseOrder', loadChildren: () => import('./PurchaseOrder/PurchaseOrder.module').then(m => m.PurchaseOrderModule) },
    
        { path: 'Reservation', loadChildren: () => import('./Reservation/Reservation.module').then(m => m.ReservationModule) },
    
        { path: 'Supplier', loadChildren: () => import('./Supplier/Supplier.module').then(m => m.SupplierModule) },
    
        { path: 'Table', loadChildren: () => import('./Table/Table.module').then(m => m.TableModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }