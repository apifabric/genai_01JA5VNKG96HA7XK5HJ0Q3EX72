import { MenuRootItem } from 'ontimize-web-ngx';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { InventoryItemCardComponent } from './InventoryItem-card/InventoryItem-card.component';

import { MenuCategoryCardComponent } from './MenuCategory-card/MenuCategory-card.component';

import { MenuItemCardComponent } from './MenuItem-card/MenuItem-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { PurchaseOrderCardComponent } from './PurchaseOrder-card/PurchaseOrder-card.component';

import { ReservationCardComponent } from './Reservation-card/Reservation-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { TableCardComponent } from './Table-card/Table-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'InventoryItem', name: 'INVENTORYITEM', icon: 'view_list', route: '/main/InventoryItem' }
    
        ,{ id: 'MenuCategory', name: 'MENUCATEGORY', icon: 'view_list', route: '/main/MenuCategory' }
    
        ,{ id: 'MenuItem', name: 'MENUITEM', icon: 'view_list', route: '/main/MenuItem' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'PurchaseOrder', name: 'PURCHASEORDER', icon: 'view_list', route: '/main/PurchaseOrder' }
    
        ,{ id: 'Reservation', name: 'RESERVATION', icon: 'view_list', route: '/main/Reservation' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'Table', name: 'TABLE', icon: 'view_list', route: '/main/Table' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CustomerCardComponent

    ,EmployeeCardComponent

    ,InventoryItemCardComponent

    ,MenuCategoryCardComponent

    ,MenuItemCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,PaymentCardComponent

    ,PurchaseOrderCardComponent

    ,ReservationCardComponent

    ,SupplierCardComponent

    ,TableCardComponent

];