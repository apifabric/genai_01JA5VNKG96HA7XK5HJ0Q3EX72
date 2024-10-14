import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Table-card.component.html',
  styleUrls: ['./Table-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Table-card]': 'true'
  }
})

export class TableCardComponent {


}