import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {MENUCATEGORY_MODULE_DECLARATIONS, MenuCategoryRoutingModule} from  './MenuCategory-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    MenuCategoryRoutingModule
  ],
  declarations: MENUCATEGORY_MODULE_DECLARATIONS,
  exports: MENUCATEGORY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class MenuCategoryModule { }