/*
 * menu_stage.h
 *
 *  Created on: Mar 30, 2022
 *      Author: Darek
 */

#ifndef MENU_STAGE_H_
#define MENU_STAGE_H_

#include "widgets/widget.h"
#include "widgets/label_widget.h"
#include "widgets/int_widget.h"
#include "widgets/float_widget.h"
#include "widgets/setting_widget.h"
#include <vector>

class LabelWidget;

namespace gui
{

class MenuContext;

constexpr size_t MAX_WIDGET_NUMBER = 8;
constexpr size_t MAX_SETTING_NUMBER = 6;

enum class EHorizontalComponentPosition
{
    CENTER,
    CUSTOM
};


struct TWidgetComponent
{
    TElementPosition position;
    EHorizontalComponentPosition horizontalComponentPosition;

    Widget* pWidget;
};

struct TSettingComponent
{
    TElementPosition labelMarkerPosition;
    TElementPosition valueMarkerPosition;
    TElementPosition valuePosition;
    SettingWidget* pValueObject;
};

class MenuStage
{

public:
    MenuStage();
    virtual ~MenuStage();

    void setContext(MenuContext* menuContext);
    void setRotation(int rotation);

    void renderStageWithRotation();

    uint8_t getSettingsNavigationIndex() const;
    void setSettingsNavigationIndex(uint8_t settingsNavigationIndex);

    virtual void buildPerspective() = 0;
    virtual void handleOkButton() = 0;
    virtual void handleUpButton() = 0;
    virtual void handleDnButton() = 0;
    virtual void handleEscButton() = 0;

protected:
    MenuContext* m_pMenuContext;

    std::vector<TWidgetComponent> m_WidgetsComponents;
    std::vector<TSettingComponent> m_SettingsComponents;

    uint8_t m_settingsNavigationIndex;
    bool m_settingEditMode;

    bool settingsNavigationMarkerIndexDecrease();
    bool settingsNavigationMarkerIndexIncrease();

    void addSingleWidget(Widget* pWidget);
    void addWidgetCoordinates(uint8_t index, uint8_t column, uint8_t page, EHorizontalComponentPosition horizontalComponentPosition = EHorizontalComponentPosition::CUSTOM);

    void addSingleSetting(SettingWidget* pValueObject);
    void addSettingCoordinates(uint8_t index, uint8_t labelMarkerColumn, uint8_t labelMarkerPage, uint8_t valueMarkerColumn, uint8_t valueMarkerPage, uint8_t valueColumn, uint8_t valuePage);

private:
    void renderStage(uint8_t* pCanvas);

    void renderWidgetComponents(uint8_t* pCanvas);
    void renderSettingComponents(uint8_t* pCanvas);
    void renderMarker(uint8_t* pCanvas);

    uint8_t determineColumnPosition(EHorizontalComponentPosition horizontalComponentPosition, size_t widgetXLength = 0);
};


} // namespace gui

#endif /* MENU_STAGE_H_ */
