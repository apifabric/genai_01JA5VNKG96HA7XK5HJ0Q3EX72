import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {INVENTORYITEM_MODULE_DECLARATIONS, InventoryItemRoutingModule} from  './InventoryItem-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    InventoryItemRoutingModule
  ],
  declarations: INVENTORYITEM_MODULE_DECLARATIONS,
  exports: INVENTORYITEM_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class InventoryItemModule { }