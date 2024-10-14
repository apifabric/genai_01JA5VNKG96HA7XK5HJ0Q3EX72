import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './MenuCategory-card.component.html',
  styleUrls: ['./MenuCategory-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.MenuCategory-card]': 'true'
  }
})

export class MenuCategoryCardComponent {


}